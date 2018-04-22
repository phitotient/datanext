import pandas as pd
import sqlalchemy
import mongodb.connectionstring as cs
import uuid
import os


class createdataframe:

    def __init__(self):
        self.engine=sqlalchemy.create_engine(cs.CONNECTION_STRING)
        currentdirectory = os.path.dirname(os.path.abspath(__file__))
        parentdirectory = os.path.dirname(currentdirectory)
        self.dataframepath=os.path.join(parentdirectory,'dataframes/')

    def gendataframeid(self):
        uid=uuid.uuid4()
        return str(uid)

    def createdataframe_csv(self,csvpath,gendataframeid):
        dataframe = pd.read_csv(csvpath)
        pathtodataframe=self.dataframepath+gendataframeid()+'.pkl'
        dataframe.to_pickle(pathtodataframe)
        return pathtodataframe


    def createdataframe_sql(self,tablename,gendataframeid):
        dataframe=pd.read_sql_table(tablename,self.engine)
        pathtodataframe=self.dataframepath+gendataframeid()+'.pkl'
        dataframe.to_pickle(pathtodataframe)
        return pathtodataframe


    def createdataframe_sqlquery(self,query,gendataframeid):
        dataframe=pd.read_sql_query(query,self.engine)
        pathtodataframe = self.dataframepath + gendataframeid() + '.pkl'
        dataframe.to_pickle(pathtodataframe)
        return pathtodataframe

    def loaddataframe(self,dataframepath):
        dataframe=pd.read_pickle(dataframepath)
        return dataframe

    def createdataframewithcolumns(self,dataframe,columns):
        pass



