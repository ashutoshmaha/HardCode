#!/usr/bin/env python
# coding: utf-8

# # Finding nearest neighbors of an incoming data point using k-Nearest Neighbors algorithm (method 2).
# 
# 
# # Ashutosh Mahajan

# In[1]:


# Add team, names, and matriculation numbers


# ## Data Preprocessing 

# ### Training Data

# In[2]:


import csv
import numpy as np
import pandas as pd

# Below is an example how data preprocessing can be achieved with pandas module
train = pd.DataFrame()
test = pd.DataFrame()

train = pd.read_csv('trainData.csv',  dtype={'Color': str,'Radius (cm)':float,'Weight (grams)':float})

#########################  DATA Preprocessing  #############################
    
# drop duplicated rows
train = train.drop_duplicates()
    
# replace zeros entries with np.nan
train = train.replace(0,np.nan)
train = train.dropna() # drop all nan entiries 
    
# transform the nominal feature (color) to dummy
newCols = pd.get_dummies(train.iloc[:,0]) 
train = pd.concat([newCols, train], axis=1) # add them to the transfomed columns to the beggining  of the data frame
train = train.drop(train.columns[3], axis = 1) # drop nominal column (color)    

## normalization
min_radius = min(train.iloc[:,3])
max_radius = max(train.iloc[:,3])
train['Radius (cm)'] = list(map(lambda x: (float(x)-min_radius)/(max_radius-min_radius), train.iloc[:,3]))

## normalization
min_weight = min(train.iloc[:,4])
max_weight = max(train.iloc[:,4])
train['Weight (grams)'] = list(map(lambda x: (float(x)-min_weight)/(max_weight-min_weight), train.iloc[:,4]))

train


# ### Test Data

# In[7]:


test = pd.DataFrame()
test = pd.read_csv('testData.csv',  dtype={'Color': str,'Radius (cm)':float,'Weight (grams)':float})

#########################  DATA Preprocessing  #############################
    
# drop duplicated rows
test= test.drop_duplicates()

# transform the nominal feature (color) to dummy
newCols=pd.get_dummies(test.iloc[:,0]) 
test = pd.concat([newCols, test], axis=1) # add them to the transfomed columns to the beggining  of the data frame
test= test.drop(test.columns[3], axis = 1) # drop nominal column (color)    

## normalization like training data
test['Radius (cm)'] = list(map(lambda x: (float(x)-min_radius)/(max_radius-min_radius), test.iloc[:,3]))

## normalization like training data
test['Weight (grams)'] = list(map(lambda x: (float(x)-min_weight)/(max_weight-min_weight), test.iloc[:,4]))

test


# # kNN Classification with K=1 and K=3.

# In[4]:


# seq=['Radius (cm)','Weight (grams)']
# train_data=pd.read_csv('trainData.csv',usecols=seq)
# display(train_data)


# In[41]:


#Euclidian distances of all the test sample 1 in test dataset with all records in training dataset:

def euc(x1,y1,x2,y2):
    euc_dist=((x1-x2)**2 + (y1-y2)**2)**.5    #sqrt(x)= x^0.5
    return(euc_dist)

a00=euc(2.5,64,2.3,61)   #assigning first incoming datapoint from test dataset to find its class.

a01=euc(2.5,64,4.8,75)   #Euclidean distance of first incoming datapoint with each record in training dataset.
a02=euc(2.5,64,3.6,173)
a03=euc(2.5,64,2.6,58)
a04=euc(2.5,64,2.1,40)
a05=euc(2.5,64,3,86)
a06=euc(2.5,64,3.1,60)
a07=euc(2.5,64,5.2,141)
a08=euc(2.5,64,2.5,70)
a09=euc(2.5,64,3.2,79)
a010=euc(2.5,64,3.9,101)
a011=euc(2.5,64,2.4,62)
a012=euc(2.5,64,4.6,152)
a013=euc(2.5,64,4.3,133)
a014=euc(2.5,64,4.1,0)
a015=euc(2.5,64,2.9,53)
a016=euc(2.5,64,4.5,110)
a017=euc(2.5,64,2.3,60)
a018=euc(2.5,64,3.7,101)
a019=euc(2.5,64,4.1,135)
a020=euc(2.5,64,2.4,63)
a021=euc(2.5,64,2.1,64)
a022=euc(2.5,64,2.7,73)
a023=euc(2.5,64,3.8,80)
a024=euc(2.5,64,402,126)
a025=euc(2.5,64,3.5,98)
a026=euc(2.5,64,3.2,62)
a027=euc(2.5,64,2.5,65)
a028=euc(2.5,64,2.1,41)
a029=euc(2.5,64,3.1,85)
a030=euc(2.5,64,0,137)
a031=euc(2.5,64,5.2,142)

all_euc=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a010,a011,a012,a013,a014,a015,a016,a017,a018,a019,a020,a021,a022,a023,a024,a025,a026,a027,a028,a029,a030,a031]
display("*********OUTPUT 1: ED of all records with incoming record 1 of the test data in order as per csv---->", all_euc)
all_euc.sort(reverse=False) #sort by increasing order
display('*********OUTPUT 2: ED of sample 1 of test data with training data in increasing order----->',all_euc)
a_near1=all_euc[0:1]   #access first nearest datapoint.
display(' *********OUTPUT 3: The ED of the nearest datapoints of sample 1 for k=1 are',a_near1)  #Lemon is the predicted class 
a_near3=all_euc[0:3]   #access first three nearest datapoints.
display('The ED of the nearest datapoints of sample 1 for k=3 are',a_near3)  #apple is the predicted class
display("! Approach: Find the pair of datapoints from OUTPUT 1 that matches OUTPUT 3 sequentially & you'll get the nearest neighbors. ")


# In[ ]:


#then we repeat the method for each new incoming datapoint by assigning it statically to the a00 variable.

#further, we can also design a function to predict the classes of the incoming datapoints.

