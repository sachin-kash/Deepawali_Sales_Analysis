#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# import data in notebook
df=pd.read_csv(r"C:\Users\sachin kashyap\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv",encoding="unicode_escape")


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


# drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[7]:


# check for null values
pd.isnull(df).sum()


# In[8]:


df.shape


# In[9]:


# drop null values
df.dropna(inplace=True)


# In[10]:


df.shape


# In[11]:


# change the data type
df['Amount'] = df['Amount'].astype('int')


# In[12]:


df['Amount'].dtypes


# In[13]:


df.columns


# In[14]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[15]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt  # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')


# # Gender

# In[17]:


ax = sns.countplot(x='Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


sales_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# # From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[19]:


df.columns


# In[20]:


ax = sns.countplot(x='Age Group', data=df, hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# # From above graphs we can see that most of the buyers are of age group between 26-35yrs female

# # State

# In[22]:


# Total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Orders')


# In[23]:


# Total anount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Amount')


# # From above grpahs we can see that most of the orders & total sales/amount are form Uttar Pradesh, Maharashtra and Karnatake respectively

# # Marital Status

# In[24]:


ax = sns.countplot(x='Marital_Status', data=df)

sns.set(rc={'figure.figsize':(7,4)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x = 'Marital_Status', y = 'Amount', data = sales_state, hue='Gender')


# # From above graphs we can see that most of the buyers are married(women) and they have high purchaing power

# # Occupation

# In[26]:


ax = sns.countplot(x='Occupation', data=df)

sns.set(rc={'figure.figsize':(8,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Occupation', y = 'Amount', data = sales_state)


# # From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x='Product_Category', data=df)


for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x = 'Product_Category', y = 'Amount', data = sales_state)


# # From above graphs we can see that most of the products are from Food, Clothing and Electronics category

# # Top saleing products

# In[32]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(5)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x = 'Product_ID', y = 'Orders', data = sales_state)


# # Conclussion: 

# # Married women age group 26-35yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food Clothing and Electronics 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




