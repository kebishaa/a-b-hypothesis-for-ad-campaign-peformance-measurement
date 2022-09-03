from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay
from fast_ml.model_development import train_valid_test_split

from scipy.stats import pearsonr
from numpy import isnan
from numpy import polyfit
from numpy import asarray

import mlflow
import dvc.api

import mlflow
import mlflow.sklearn
import logging

from matplotlib import pyplot as plt
from urllib.parse import urlparse
import seaborn as sns
import pandas as pd
import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join("./scripts")))
import preprocess
from models import BuildModels
bm = BuildModels('classifier')

mlflow.set_experiment('mlops-abtest')

# get the list of models to consider
models = bm.get_models()

path = 'data/AdSmartABdata.csv'
repo = 'https://github.com/10-Academy-B6-W2-Team-10/a-b-hypothesis-for-ad-campaign-peformance-measurement.git'
versions = ['v1','v2','v3','v4','v5']


for v in versions:
    data_url = dvc.api.get_url(
        path=path,
	repo=repo,
	rev=v
    )
    
    ## Read data
    # data = pd.read_csv(data_url, sep=',')
    data = pd.DataFrame()
    with dvc.api.open(path=path, repo=repo, rev=v) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        rows = []
        for row in csv_reader:
            rows.append(row)

        data = pd.DataFrame(rows, columns=header)
# preprocess
    data = preprocess.remove(data, ['auction_id', 'date', 'hour', 'no'])
    data = preprocess.encode(data, 'experiment')
    data = preprocess.encode(data, 'device_make')
    data = preprocess.encode(data, 'platform_os')
    data = preprocess.encode(data, 'browser')

    ## Spliting the data
    X_train, y_train, X_valid, y_valid, X_test, y_test = train_valid_test_split(
        data, target='yes', train_size=0.7, valid_size=0.20, test_size=0.10)
    
    y_test = y_test.astype('int')#[int(yt) for yt in y_test]
    y_train = y_train.astype('int')#[int(yt) for yt in y_train]
    
    print("X_train shape: ", X_train.shape), print(
        "y_train shape: ", y_train.shape)
    print("X_valid shape: ", X_valid.shape), print(
        "y_valid shape: ", y_valid.shape)
    print("X_test shape: ", X_test.shape), print(
        "y_test shape: ", y_test.shape)

    with mlflow.start_run():
        # Log data params
        mlflow.log_param("data_url", data_url)
        mlflow.log_param("data_version", v)
        mlflow.log_param("data_rows", data.shape[0])
        mlflow.log_param("data_cols", data.shape[1])
        
        # evaluate each model
        for model in models:
            grid_values, grid_clf_acc = bm.grid_search(model[0], model[1])
            grid_clf_acc.fit(X_train, y_train)
            
            mlflow.log_param('best param for '+model[0],grid_clf_acc.best_params_)
            #Predict values based on new parameters
            y_pred_acc = grid_clf_acc.predict(X_test)
            
            y_pred_acc = [int(pred) for pred in y_pred_acc]
            # New Model Evaluation metrics
            print('Model Metrics for '+model[0]+" with data version "+v+'\n')
            print('Accuracy Score : ' + str(accuracy_score(y_test, y_pred_acc)))
            print('Precision Score : ' + str(precision_score(y_test, y_pred_acc)))
            print('Recall Score : ' + str(recall_score(y_test, y_pred_acc)))
            print('F1 Score : ' + str(f1_score(y_test, y_pred_acc)))

            #Logistic Regression (Grid Search) Confusion matrix
            cm = confusion_matrix(y_test, y_pred_acc)
            
            disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels = grid_clf_acc.classes_)
            disp.plot()
            
            plt.savefig('./images/confusion_matrics_'+model[0]+'_'+v+'.png')
            plt.close()

            # Writing to file
            with open("./models/metrics.txt", "a") as file1:
                # Writing data to a file
                file1.write('Model Metrics for '+model[0]+" with data version "+v+'\n')
                file1.write("accuracy is %2.1f%% \n" %
                            accuracy_score(y_test, y_pred_acc))
                file1.write("precision is %2.1f%% \n" %
                            precision_score(y_test, y_pred_acc))
                file1.write("recall is %2.1f%% \n" %
                            recall_score(y_test, y_pred_acc))
                file1.write("F1 Score %2.1f%% \n" % 
                            f1_score(y_test, y_pred_acc))
            
            mlflow.log_metric("acc",  accuracy_score(y_test, y_pred_acc))
            mlflow.log_metric("prec",  precision_score(y_test, y_pred_acc))
            mlflow.log_metric("recall", recall_score(y_test, y_pred_acc))
            mlflow.log_metric("F1 Score", f1_score(y_test, y_pred_acc))

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    grid_clf_acc, model[0], registered_model_name=model[0])
            else:
                mlflow.sklearn.log_model(model[1], model[0])
