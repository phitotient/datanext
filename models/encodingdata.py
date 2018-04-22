import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder


class encodingdata:

    def autolabelencoding(self,dataframe,columns_encoded):
        dataset=dataframe
        encoding=columns_encoded
        for var in encoding:
            number = LabelEncoder()
            dataset[var] = number.fit_transform(dataset[var].astype('str'))
        return dataset


# Function takes dictionary of columns in given format and encodes according to the dictionary passed Example for dictionary to be passed:
# Ex-: cleanup_nums = {"num_doors": {"four": 4, "two": 2}}


    def labelencoding(self,dataframe,dictionary_columns_encoded):
        dataset=dataframe
        dataset.replace(dictionary_columns_encoded,inplace=True)
        return dataset

    def onehotencoding(self,dataframe,columns_encoded):
        dataset=dataframe
        encoding=columns_encoded
        onehotdataframe=pd.get_dummies(dataset, columns=encoding)
        return onehotdataframe

    def handlingnulls(self,dataframe):
        pass


    def describedata(self,dataframe):
        dataset=dataframe.describe(include='all')
        jsondata=dataset.to_json(orient='index')
        return jsondata


