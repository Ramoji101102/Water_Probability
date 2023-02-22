#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbs

data = pd.read_csv(r'C:\Users\Administrator\Downloads\pyhon\water_potability.csv')


# In[9]:


data


# In[10]:


data.shape


# #Data cleaning

# In[12]:


data.info()


# In[13]:


data.head()


# In[15]:


data.isnull().sum()


# In[18]:


data.fillna(data.mean(),inplace=True)


# In[16]:


data.describe()


# In[ ]:





# In[23]:


sbs.heatmap(data.corr(),annot=True,cmap='terrain')
fig=plt.gcf()
fig.set_size_inches(11,6)
plt.show()


# In[25]:


data.boxplot(figsize=(15,6))
plt.show()


# In[27]:


data['Solids'].describe()


# In[28]:


data['Solids']


# In[ ]:





# In[32]:


data['Potability'].value_counts()


# In[35]:


df.Potability.value_counts().plot(kind="bar",color=["brown","salmon"])


# In[39]:


sbs.countplot(data['Potability'])
plt.show()


# In[40]:


data.hist(figsize=(14,12))
plt.show()


# In[34]:


sbs.barplot(x=data['ph'],y=data['Hardness'],hue=data['Potability'])
plt.show()


# In[ ]:


df.Potability.value_counts().plot(kind="bar",color)

