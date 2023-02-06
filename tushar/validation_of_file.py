#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import json
import shutil
import re
import pandas as pd


# In[10]:


with open('C:\Personal\Data Sc\D_Banyan\Dbanyan\Projects\schema_cred.json','r') as json_file:
    schema =json.load(json_file)


# In[11]:


os.chdir(r"C:\Personal\Data Sc\D_Banyan\Dbanyan\Projects\Datasets")


# In[12]:


good_path = r"C:\Personal\Data Sc\D_Banyan\Dbanyan\Projects\validated-raw-data\validated-matched"
bad_path = r"C:\Personal\Data Sc\D_Banyan\Dbanyan\Projects\validated-raw-data\validated-unmatched"
data_path=os.listdir('C:\Personal\Data Sc\D_Banyan\Dbanyan\Projects\Datasets')


# In[13]:


def filevalidation(data_path,schema):
    for file in data_path:
        df=pd.read_csv(file)
        length_df = df.shape[1]
        schema_len=schema['numberofcolumns']
        pattern = r'^Retail_data\.csv$'
        pattern1= r'^Retail_data\d\.csv$'
        if (re.match(pattern , file) is not None) or (re.match(pattern1 , file) is not None):
            splitname=re.split('_',file)
            if len(splitname[0])== schema['lenoffilenameb']:
                if schema_len==length_df:
                    if list(df)==list(schema['columns']):
                        for col in list(df):
                            if df[col].dtype == schema['columns'][col]:
                                os.makedirs(good_path,exist_ok=True)
                                shutil.copy( src= file, dst= good_path)
                            else:
                                print(f"{col}-{df[col].dtype} -----> {col}-{schema['columns'][col]}")
                                os.makedirs(bad_path,exist_ok=True)
                                shutil.copy(src = file,dst = bad_path)
                    else:
                        os.makedirs(bad_path,exist_ok=True)
                        shutil.copy(src = file,dst = bad_path)
                else:
                    os.makedirs(bad_path,exist_ok=True)
                    shutil.copy( src=file, dst= bad_path)
            else:
                os.makedirs(bad_path,exist_ok=True)
                shutil.copy( src=file, dst= bad_path)
        else:
            os.makedirs(bad_path,exist_ok=True)
            shutil.copy( src=file, dst= bad_path)


# In[14]:


filevalidation(data_path,schema)

