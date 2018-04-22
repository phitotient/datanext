from tpot import TPOTClassifier
from tpot import TPOTRegressor
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import sys


class runmodel:

    def __init__(self):
        self.tpotclassifier=TPOTClassifier(generations=5,verbosity=2,population_size=20,random_state=7)
        self.tpotregressor=TPOTRegressor(generations=5,verbosity=2,population_size=20,random_state=7)

    def regressor(self,dataframe,target):
        x=dataframe.drop(target,axis=1)
        y=dataframe[[target]]
        X_train, X_test, y_train, y_test = train_test_split(x,y,train_size=0.75, test_size=0.25)
        self.tpotregressor.fit(X_train, y_train)
        bestscore=self.tpotregressor.score(X_test, y_test)
        return bestscore


    def classifier(self,dataframe,target):
        x=dataframe.drop(target,axis=1)
        y=dataframe[[target]]
        X_train, X_test, y_train, y_test = train_test_split(x, y,train_size=0.75, test_size=0.25)
        self.tpotclassifier.fit(X_train, y_train)
        bestscore=self.tpotclassifier.score(X_test, y_test)
        return bestscore
