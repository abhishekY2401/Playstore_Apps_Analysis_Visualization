#!/usr/bin/env python
# coding: utf-8

# In[124]:


#importing the required packages
import pandas as pd
import numpy as np


# # Creating a dataframe for each of the dataset

# In[125]:


#creating a dataframe of the playstore apps data
df1=pd.read_csv("playstore_apps.csv")
df1


# In[126]:


#creating a dataframe of the playstore reviews data
df2=pd.read_csv("playstore_reviews.csv",index_col='App')
df2


# # Data Cleaning-Playstore App Dataset

# First, we have done the preprocessing for the Playstore App Dataset

# In[127]:


#removing the duplicates from the playstore app dataset
df1.drop_duplicates(keep='first',inplace=True)
df1.info()


# This shows that after dropping the duplicates there are some null values present. Let us now see the number of null values in each column.

# In[128]:


#checking the number of null values in each column 
df1.isnull().sum()


# Here, we can see that Rating column has the highest number of null values. These values can be filled with 0.0, the least rating.

# In[129]:


#replacing the null values in the rating column with '0.0'
df1['Rating'] = df1['Rating'].fillna(0.0)


# Now, as asked in the question, we are keeping the NaN values found in 'Current Ver' column as it is, but removing the null values in the other columns 

# In[132]:


#removing all the null values in the playstore app dataset except for the 'Çurrent ver' row
df1=df1.dropna(subset=['Reviews','Installs','Type','Price','Content Rating','Last Updated','Android Ver'])


# In[133]:


#confirming that the 'current ver' row is the obnly row with null values
df1[df1.isna().any(axis=1)]


# # Checking for Unique Values in Each Column-Playstore App dataset

# If there are values in a column that do are irrelevant to the other values in that column, then we are excluding the row.

# In[134]:


print(df1['Category'].unique())


# In[135]:


print(df1['Rating'].unique())


# In[136]:


df1['Reviews'].unique()


# In[137]:


print(df1['Size'].unique())


# In[138]:


df1['Installs'].unique()


# In[139]:


df1['Type'].unique()


# In[140]:


df1['Price'].unique()


# In[141]:


df1['Content Rating'].unique()


# In[142]:


df1['Genres'].unique()


# In[143]:


df1['Last Updated'].unique()


# In[144]:


df1['Current Ver'].unique()


# In[145]:


df1['Android Ver'].unique()


# We found that all the columns contain relevant data, so this ensures that our datasets are preprocessed.

# # Data Cleaning-Playstore Reviews Dataset

# In[146]:


#checking which rows have null values in the playstore reviews dataset
df2[df2.isna().any(axis=1)]


# Removing all these Null values would ensure clean data

# In[147]:


#dropping the null values in the playstore reviews dataset
df2.dropna(inplace=True)


# In[148]:


df2.isnull().sum()


# Now there are no null values present in the dataset. We decided not to drop the duplicates in this dataset, as doing so is removing all the important information about the Sentiment and reviews, i.e, there is a possibility that for the same app there are two reviews and sentiments which are same but given by two different users of that app. By dropping duplicates, we will lose this information though they might not be duplicates.

# # Checking for Unique Values-Playstore Reviews Dataset

# If there are values in a column that do are irrelevant to the other values in that column, then we are excluding the row.

# In[119]:


df2['Translated_Review'].unique()


# In[120]:


df2['Sentiment'].unique()


# In[121]:


df2['Sentiment_Polarity'].unique()


# In[122]:


df2['Sentiment_Subjectivity'].unique()


# We found that all the columns contain relevant data, so this ensures that our datasets are preprocessed.

# # Exporting both the cleaned files 

# In[89]:


df1.to_csv('Updated Playstore_Apps.csv')


# In[93]:


df2.to_csv('Updated Playstore_Reviews.csv')


# In[ ]:




