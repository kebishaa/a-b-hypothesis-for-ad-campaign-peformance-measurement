# Get url from DVC
from asyncio.log import logger
import warnings
import mlflow
import os
from random import random, randint
import dvc.api

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

# To evaluate end result we have
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score


path='data/AdSmartABdata.csv'
repo='/home/jds98/10 Academy/Week 2/a-b-hypothesis-for-ad-campaign-peformance-measurement'
version='v1'

data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)

mlflow.set_experiment('mlops-abtest')

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    ## Read data
    data = pd.read_csv(data_url, sep=',')
	
	# Log data params
    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)
    mlflow.log_param("data_rows", data.shape[0])
    mlflow.log_param("data_cols", data.shape[1])


    ## Spliting the data
    from fast_ml.model_development import train_valid_test_split

    X_train, y_train, X_valid, y_valid, X_test, y_test = train_valid_test_split(data, target = 'SalePrice', 
                                                                                train_size=0.8, valid_size=0.1, test_size=0.1)

    print(X_train.shape), print(y_train.shape)
    print(X_valid.shape), print(y_valid.shape)
    print(X_test.shape), print(y_test.shape)

    # Log artifacts: columns used for modeling
    cols_x = pd.DataFrame(list(X_train.columns))
    cols_x.to_csv('features.csv', header=False, index=False)
    mlflow.log_artifact('features.csv')

    cols_y = pd.DataFrame(list(y_train.columns))
    cols_y.to_csv('targets.csv', header=False, index=False)
    mlflow.log_artifact('targets.csv')

	# Log an artifact (output file)
    if not os.path.exists("outputs"):
	    os.makedirs("outputs")
#	with open("outputs/test.txt", "w") as f:
#		f.write("hello world!")
	log_artifacts("outputs")
	

