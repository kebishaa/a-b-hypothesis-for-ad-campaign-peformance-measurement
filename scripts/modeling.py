from sklearn.metrics import classification_report
from tkinter import font
import preprocess

# Get url from DVC
from asyncio.log import logger
import warnings

import csv
import os
import sys
from random import random, randint
import dvc.api

import mlflow
import mlflow.sklearn
import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Importing Pandas an Numpy Libraries to use on manipulating our Data
import pandas as pd
import numpy as np

# Image Disp
from IPython.display import Image

# To Preproccesing our data
from sklearn.preprocessing import LabelEncoder

# To fill missing values
from sklearn.impute import SimpleImputer

# To Split our train data
from sklearn.model_selection import train_test_split
from fast_ml.model_development import train_valid_test_split

# To Visualize Data
import matplotlib.pyplot as plt
import seaborn as sns

# To Train our data
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from urllib.parse import urlparse

# To evaluate end result we have
from sklearn.metrics import accuracy_score, confusion_matrix,mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score

# import custom function
# sys.path.append(os.path.abspath(os.path.join("../scripts")))
import preprocess

path = 'data/AdSmartABdata.csv'
repo = '/Users/user/TENAC/week-1-4/Week-2/a-b-hypothesis-for-ad-campaign-peformance-measurement'
version='v1'

data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)
    
mlflow.set_experiment('mlops-abtest')


def eval_metrics(actual, pred):
    tn, fp, fn, tp = confusion_matrix(actual,pred).ravel()
    return {'acc':(tp+fp)/(tn+tp+fn+fp), 'prec':tp/(tp+fp),'rec':tp/(tp+fn)}

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    ## Read data
    # data = pd.read_csv(data_url, sep=',')
    data = pd.DataFrame()
    with dvc.api.open(path=path, repo=repo, rev=version) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        rows = []
        for row in csv_reader:
            rows.append(row)

        data = pd.DataFrame(rows, columns=header)
 
    data = preprocess.remove(data, ['auction_id','date', 'hour','no'])
    data = preprocess.encode(data, 'experiment')
    data = preprocess.encode(data, 'device_make')
    data = preprocess.encode(data, 'platform_os')
    data = preprocess.encode(data, 'browser')
    print(data.head())
    ## Spliting the data
    from fast_ml.model_development import train_valid_test_split

                                                 
    ## Spliting the data
    X_train, y_train, X_valid, y_valid, X_test, y_test = train_valid_test_split(data, target = 'yes', train_size=0.7, valid_size=0.20, test_size=0.10)

    print("X_train shape: ", X_train.shape), print("y_train shape: ", y_train.shape)
    print("X_valid shape: ", X_valid.shape), print("y_valid shape: ", y_valid.shape)
    print("X_test shape: ", X_test.shape), print("y_test shape: ", y_test.shape)

    print("X_train shape: ", X_train.shape), print("y_train shape: ", y_train.shape)
    print("X_valid shape: ", X_valid.shape), print("y_valid shape: ", y_valid.shape)
    print("X_test shape: ", X_test.shape), print("y_test shape: ", y_test.shape)

    with mlflow.start_run():
        # Log data params
        mlflow.log_param("data_url", data_url)
        mlflow.log_param("data_version", version)
        mlflow.log_param("data_rows", data.shape[0])
        mlflow.log_param("data_cols", data.shape[1])
        
        lr = LogisticRegression(random_state=42)
        lr.fit(X_train, y_train)
        
        labels = X_train.columns
        importance = lr.coef_
        feature_df = pd.DataFrame(list(zip(labels,importance[0])),columns=['features','importance'])
        feature_df = feature_df.sort_values('importance',ascending=False)
        
        ax =sns.barplot(x='importance',y='features',data=feature_df)
        ax.set_xlabel('Importance',fontsize=18)
        ax.set_ylabel('Feature', fontsize=18)
        ax.set_title('rf f-i', fontsize=22)
        plt.tight_layout()
        plt.savefig('./images/fi.png')
        plt.close()
        
        predicted_qualities = lr.predict(X_test)

        evaluatin_dict = eval_metrics(y_test, predicted_qualities)
        
        # Writing to file
        with open("./models/metrics.txt", "w") as file1:
            # Writing data to a file
            file1.write("accuracy is %2.1f%% \n" % evaluatin_dict['acc'] )
            file1.write("precision is %2.1f%% \n" % evaluatin_dict['prec'])
            file1.write("recall is %2.1f%% \n" % evaluatin_dict['rec'])

        print("  acc: %s" % evaluatin_dict['acc'])
        print("  precision: %s" % evaluatin_dict['prec'])
        print("  recall: %s" % evaluatin_dict['rec'])

        mlflow.log_metric("acc",  evaluatin_dict['acc'])
        mlflow.log_metric("prec", evaluatin_dict['prec'])
        mlflow.log_metric("recall", evaluatin_dict['rec'])

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(
                lr, "model", registered_model_name="ElasticnetWineModel")
        else:
            mlflow.sklearn.log_model(lr, "model")

