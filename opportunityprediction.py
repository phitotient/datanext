import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE



train=pd.read_csv("opportunity.csv")
cat_cols=['Fiscal_Month','Project_State','deal_rating','designation','industry','new_project','product','daysforconversion']
for var in cat_cols:
    number = LabelEncoder()
    train[var] = number.fit_transform(train[var].astype('str'))
train.to_csv('encodedoppor.csv',index=False)

X = train.drop('daysforconversion', axis=1)
y = train[['daysforconversion']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
regression_model = LinearRegression(normalize=False)
regression_model.fit(X_train, y_train)

for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))
print(X_test)
print(regression_model.predict([[4, 5, 3, 2, 6, 4, 0, 0.25, 0.25,1]]))





