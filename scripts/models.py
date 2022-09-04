# To Train our data
from statistics import mean
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import evaluation_metrics

import numpy as np


class BuildModels:
    def __init__(self,mtype:str):
        self.mtype = mtype
        
    def get_models(self):
        models = list()
        # models.append(['logistic regression',LogisticRegression()])
        # models.append(['decision tree',DecisionTreeClassifier()])
        # models.append(['random forest',RandomForestClassifier()])
        models.append(['xgboost',XGBClassifier()])
        return models
   
    def grid_search(self,mtype:str,model):
        
       if mtype == 'logistic regression':
            grid_values = {'penalty': ['l2'], 'C': [0.001, .009, 0.01, .09, 1, 5, 10]}
            grid_clf_acc = GridSearchCV(model, param_grid=grid_values, scoring='recall')
            return grid_values, grid_clf_acc
       
       elif mtype == 'decision tree':
            grid_values = {'criterion': ['gini', 'entropy'], 
                           'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30]}
            grid_clf_acc = GridSearchCV(model, param_grid=grid_values, scoring='recall')
            return grid_values, grid_clf_acc
        
       elif mtype == 'random forest':
           grid_values = {'n_estimators': [100,200], 
                          'max_features': ['auto', 'sqrt'],
                          'max_depth': [4, 5, 15, 20],
                          'min_samples_split': [2, 5, 10] , 
                          'min_samples_leaf': [1, 2, 4], 
                          'bootstrap': [True, False]}
           
           grid_clf_acc = GridSearchCV(model, param_grid=grid_values, scoring='recall')
           return grid_values, grid_clf_acc
       
       elif mtype=='xgboost':
           grid_values = {"subsample": [0.5, 0.75, 1],
                         "colsample_bytree": [0.5, 0.75, 1],
                         "max_depth": [2, 6, 12],
                         "min_child_weight": [1, 5, 15],
                         "learning_rate": [0.3, 0.1, 0.03],
                         "n_estimators": [100]}
           grid_clf_acc = GridSearchCV(model, param_grid=grid_values, scoring='recall')
           return grid_values, grid_clf_acc
           
    #  evaluate the model using a given test condition
    def evaluate_model(self, cv, model,data):
        # get the dataset
        X, y = data[0],data[1]
        # evaluate the model
        scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
        # return scores
        return mean(scores)