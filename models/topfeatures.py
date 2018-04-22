"""

This script takes a dataframe and finds out top n features using recursive elimination according to users
given value of n

"""
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pandas as pd

class topfeatures:

    def findtopfeatures_csv(self,dataframe,numberoffeatures):
        array=dataframe.values
        x = array[:,0:len(list(dataframe))-1]
        y = array[:,len(list(dataframe))-1]

        # create a base classifier used to evaluate a subset of attributes
        model=LogisticRegression()

        # create the RFE model and select 3 attributes
        rfe = RFE(model,numberoffeatures)
        rfe = rfe.fit(x, y)
        # summarize the selection of the attributes
        return rfe.support_,rfe.ranking_
