import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[3]:


data=pd.read_csv('/home/nikhithabalagani/parkinsons.csv')


# In[4]:


data.head()


# In[5]:


features=data.loc[:,data.columns!='status'].values[:,1:]
labels=data.loc[:,'status'].values


# In[6]:


print(labels[labels==1].shape[0],labels[labels==0].shape[0])


# In[7]:


scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels


# In[8]:


x_train,x_test,y_train, y_test= train_test_split(x,y,test_size=0.2, random_state=7)


# In[9]:


model= XGBClassifier()
model.fit(x_train, y_train)


# In[10]:


y_pred=model.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)


# In[11]:


import pickle
pickle.dump(model,open('model.pk1','wb'))


