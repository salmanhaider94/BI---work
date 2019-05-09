#!/usr/bin/env python
# coding: utf-8

# In[2]:


#SYED SALMAN HAIDER
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv('BigML.Churn.csv')


# In[28]:


df.head(6)


# In[29]:


df.isna().sum()


# In[30]:


df.shape


# In[31]:


df.describe()


# In[32]:


df['State'].describe()


# In[33]:


df.head(5)


# In[34]:


df['International plan']= df['International plan'].replace('No','No International Plan')
df['International plan']= df['International plan'].replace('Yes','International Plan')

df['Voice mail plan']= df['Voice mail plan'].replace('No','No Voice mail Plan')
df['Voice mail plan']= df['Voice mail plan'].replace('Yes','Voice mail Plan')


# In[35]:


df.head(6)


# In[41]:


plt.hist(df['Churn'].astype(int))
#this shows there are more people who don't churn (0,false)compared to those who have churned (1,true)


# In[42]:


df.to_csv('ChurnBI-salman')


# In[ ]:




