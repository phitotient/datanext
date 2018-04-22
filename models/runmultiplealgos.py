import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from models.createdataframe import createdataframe
import json


class runmultiplealgos:

    def __init__(self):
        self.cd=createdataframe()
        self.seed=7
        self.scoring='accuracy'
        self.models=[]
        self.results=[]
        self.names=[]
        self.finalresultsmean=[]
        self.finalresultsstd = []

    def classifier(self,dataframe):
        array = dataframe.values
        X = array[:,0:len(list(dataframe))-1]
        Y = array[:,len(list(dataframe))-1]
        # prepare configuration for cross validation test harness
        # prepare models
        self.models.append(('LR', LogisticRegression()))
        self.models.append(('LDA', LinearDiscriminantAnalysis()))
        self.models.append(('KNN', KNeighborsClassifier()))
        self.models.append(('CART', DecisionTreeClassifier()))
        self.models.append(('NB', GaussianNB()))
        self.models.append(('SVM', SVC()))
        # evaluate each model in turn
        for name, model in self.models:
            kfold = model_selection.KFold(n_splits=10, random_state=self.seed)
            cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=self.scoring)
            self.names.append(name)
            self.finalresultsmean.append(cv_results.mean())
            self.finalresultsstd.append(cv_results.std())
        results=json.dumps({"algos":self.names,"result_mean":self.finalresultsmean,"standard_deviation":self.finalresultsstd})
        return results


