import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

class leadprediction:
    def __init__(self, namevalue):
        self.namevalue = namevalue

    def trainmodel(self):
        annual_revenue=self.namevalue["AmountDefault"]
        riskrating=self.namevalue["RiskRating"]
        limit_usage=self.namevalue["LimitUsage"]
        ebita_margin=self.namevalue["Ebita"]
        State=self.namevalue["ga_state"]
        Country=self.namevalue["ga_country"]
        email_status=self.namevalue["EmailOptOut"]
        fax_status=self.namevalue["Faxoptout"]
        mail_status=self.namevalue["Mail_status"]
        phone_status=self.namevalue["SMSOptOut"]
        est_value=self.namevalue["est_value"]
        Industry=self.namevalue["IndustryID"]
        job_title=self.namevalue["Job_title"]
        lead_source=self.namevalue["ga_source"]
        no_of_employees=self.namevalue["employee_no"]
        Rating=self.namevalue["RatingID"]
        Islisted=self.namevalue["ga_company_status"]

        train=pd.read_csv("lead.csv")
        cat_cols=['RiskRating','State','Country','Do not allow E-mails','Do not allow Faxes','Do not allow Mails','Do not allow Phone Calls','Industry','Job Title','Lead Source','Rating']
        for var in cat_cols:
            number = LabelEncoder()
            train[var] = number.fit_transform(train[var].astype('str'))
        train.to_csv('encoded.csv',index=False)
        array=train.values
        x=array[:,0:17]
        y=array[:,17]
        svc=SVC(probability=True)
        leadsvc=svc.fit(x,y)
        predictedprobability=svc.predict_proba([[150000,0,53,16,0,1,1,0,0,1,0,44000,5,2,0,43,2]])
        return(predictedprobability[0][0])

