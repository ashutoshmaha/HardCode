#!/usr/bin/env python
# coding: utf-8

# # Heart Failure Prediction Dataset Data Cleaning & Visualization
# # Ashutosh Mahajan

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv(r'C:\Users\mahaj\Downloads\HFP\heart_failure_clinical_records_dataset.csv')
pd.set_option('display.max_rows', None)

display(df)


# In[3]:


#Adding serial numbers to the rows
df.insert(0, 'Sr_No', range(0, 0 + len(df)))
display(df)


# In[4]:


#Renaming columns according to proper casing
df.rename(columns={'age':'Age','anaemia':'Anaemia','creatinine_phosphokinase':'Creatinine_Phosphokinase','diabetes':'Diabetes','ejection_fraction':'Ejection_Fraction','high_blood_pressure':'High_Blood_Pressure','platelets':'Platelets','serum_creatinine':'Serum_Creatinine','serum_sodium':'Serum_Sodium','sex':'Sex','smoking':'Smoking','time':'Years_Since'},inplace=True)
display(df)


# In[5]:


#Converting Age from float to integer and Serum_Sodium from int to float type
df['Age'] = df['Age'].astype(int) 
df['Serum_Sodium'] = df['Serum_Sodium'].astype(float) 

# df['Anaemia'].dtype

#Replacing 0 with No and 1 with yes
df['Anaemia'] = df['Anaemia'].astype(str)      #column Anaemia      
df["Anaemia"]= df["Anaemia"].replace('0', 'No') 
df["Anaemia"]= df["Anaemia"].replace('1', 'Yes') 

df['Diabetes'] = df['Diabetes'].astype(str)     #column Diabetes      
df["Diabetes"]= df["Diabetes"].replace('0', 'No') 
df["Diabetes"]= df["Diabetes"].replace('1', 'Yes') 

df['High_Blood_Pressure'] = df['High_Blood_Pressure'].astype(str)     #column High_Blood_Pressure      
df["High_Blood_Pressure"]= df["High_Blood_Pressure"].replace('0', 'No') 
df["High_Blood_Pressure"]= df["High_Blood_Pressure"].replace('1', 'Yes') 

df['Sex'] = df['Sex'].astype(str)     #column Sex      
df["Sex"]= df["Sex"].replace('0', 'Female') 
df["Sex"]= df["Sex"].replace('1', 'Male') 

df['Smoking'] = df['Smoking'].astype(str)     #column Smoking      
df["Smoking"]= df["Smoking"].replace('0', 'No') 
df["Smoking"]= df["Smoking"].replace('1', 'Yes') 

df['DEATH_EVENT'] = df['DEATH_EVENT'].astype(str)     #column DEATH_EVENT      
df["DEATH_EVENT"]= df["DEATH_EVENT"].replace('0', 'No') 
df["DEATH_EVENT"]= df["DEATH_EVENT"].replace('1', 'Yes') 

display(df)


# In[6]:


#Conditioning the dataset as per the scenario


# In[7]:


#Suppose, we select the patients with age 80 or above who do not smoke and has no diabetes
above60 = df[(df.Age >= 80) & (df.Diabetes == 'No')  & (df.Smoking == 'No')]
display(above60)


# In[8]:


#Mean for columns Creatinine_Phosphokinase, Platelets and Serum_Creatinine

cp_mean=df['Creatinine_Phosphokinase'].mean()
p_mean=df['Platelets'].mean()
sc_mean=df['Serum_Creatinine'].mean()
print('Creatinine_Phosphokinase:',cp_mean,'units/L')
print('Platelets:',p_mean,'mcL')
print('Serum_Creatinine:',sc_mean,'mg/dL')


# In[9]:


# Data Visualization


# In[10]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# import seaborn
import numpy


# In[11]:


# Scatterplot depicting Ejection Fraction according to age for dataset above60:

#(An ejection fraction is the volumetric fraction of fluid ejected from a chamber with each contraction.
#It can refer to the cardiac atrium, ventricle, gall bladder, or leg veins, although if unspecified it 
#usually refers to the left ventricle of the heart. Source: Wikipedia)

arr2= above60["Age"].to_numpy()
arr2
arr3= above60["Ejection_Fraction"].to_numpy()
arr3


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])

ax.scatter(arr2, arr3 ,color='r', marker='^')
ax.scatter(arr2, arr2, color='b', marker='x')
ax.set_xlabel('Age (Years)')
ax.set_ylabel('Ejection_Fraction (mg/dL)')
ax.set_title('scatter plot')
plt.grid(True)
plt.show()
