#!/usr/bin/env python
# coding: utf-8

# # Finding nearest neighbors of an incoming data point using k-Nearest Neighbors algorith(method 1).
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

# In[3]:


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


# In[4]:


import pandas as pd

df=pd.DataFrame(train)
new_training=df[["Radius (cm)","Weight (grams)","Green","Red","Yellow"]]
new_df=new_training.copy()  #copying records of training dataset to new dataframe to sort the sequence.
new_df


# In[21]:


in_list=new_df.values.tolist()  #convert dataframe to list form
display(in_list)


# In[25]:


# calculate the Euclidean distance between two vectors:

def euc_dist(row1, row2):        #function for ED of first record in training dataset with other records.
    s = 0.0                      #We must add each records from test dataset statically to 0th row in new_df.
    for i in range(len(row1)-3):          #selecting columns except last 3              
        s += (row1[i] - row2[i])**2  
        s_r= s**0.5                       #sqrt(x)= x^0.5
    return(s_r)


rowx = in_list[0]
display("Below are the euclidian distances of first record with rest : ")   #ED of the the first record with all the other samples 
for row in in_list:                                                         #in form of aa,ab,ac,ad,ae,af and so on.
    distance = euc_dist(rowx, row) 
    display(distance)


# In[23]:


def call_neighbors(training, testing, in_vicinity):
    howfar = list()
    for train_row in training:
        dist = euc_dist(testing, train_row)
        howfar.append((train_row, dist))
    howfar.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(in_vicinity):
        neighbors.append(howfar[i][0])
    return neighbors

# for k=3
neighbors=call_neighbors(in_list,in_list[0],3)
for members in neighbors:
    print(members[0:2],'\n')
print("Above is the set of closest 3 data members.")

# for k=1
neighbors=call_neighbors(in_list,in_list[0],1)
for members in neighbors:
    display(members[0:2])
display("Above is the closest 1 data member.")


# In[ ]:


#process will continue by statically adding incoming datapoints to 0th row in dataframe new_df.

#further, we can also design a function to predict the classes of the incoming datapoints.

