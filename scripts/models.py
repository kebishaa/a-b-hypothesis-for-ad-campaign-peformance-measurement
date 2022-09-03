# To Train our data
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV

import evaluation_metrics

class BuildModels:
    def __init__(self,mtype:str, data_version:str, data:list):
        self.mtype = mtype
        self.data_version = data_version
        self.data = data
    
    def build_model(self,mtype:str):
        
        if mtype == 'lr':
            print('logistic regression')
            clf = LogisticRegressionCV(cv=5, random_state=0).fit(self.data[0], self.data[1])
            return clf
        
        if mtype == 'dt':
            print('Decision Trees')
            
        if mtype == 'xg':
            print('XGBoost')
        if mtype=='rf':
            print('Random Forest')
        
        #  pred = clf.prediction(self.data[2])
            # accuracy,precision,recall = evaluation_metrics.eval_metrics(self.data[3],pred)