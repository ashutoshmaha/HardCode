#!/usr/bin/env python
# coding: utf-8

# Calling API, Conversion of data

# In[1]:


import requests
import json

with open("A:/recruitment_challenge-master/recruitment_challenge-master/BI_IHC_202109/customer_journeys_sample.json") as j:
    customer_journeys= json.load(j)
customer_journeys


# In[2]:


# api_keyq ='db9e5066-4dec-4e75-85a5-0fe8d28bda8d'
api_keyq ='e57757b1-a44a-4c76-aa98-8efbe3cd2d16'

## Insert Conversion Type ID here
conv_type_id ='AM'

api_url ="https://api.ihc-attribution.com/v1/compute_ihc?conv_type_id=AM".format(conv_type_id=conv_type_id)


# In[3]:


body = {
    'customer_journeys':customer_journeys
}

response = requests.post(
    api_url , 
    data=json.dumps(body), 
    headers= {
        'Content-Type': 'application/json',    
        'x-api-key': api_keyq
    }
)

results = response.json()

print(f"Status Code:{results['statusCode']}")

print("-"*30)

print(f"Partial Failure Errors:{results['partialFailureErrors']}")
print("-"*30)
display(results['value'])


# In[4]:


ihc_results = json.loads(response.content)
# ihc_results    
# display(ihc_results)
# type(ihc_results)


# In[5]:


pop1=ihc_results.pop("value")
pop1
type(pop1)


# 2. Processing the Data

# In[6]:


import pandas as pd 

df_attribution_results = []

for i in pop1:
    df_ihc_results = pd.DataFrame.from_dict(pop1)
    df_attribution_results.append(df_ihc_results)
df_attribution_results = pd.concat(df_attribution_results)

df_attribution_results.head(5)


# In[ ]:





# In[7]:


#Assumption: each unique conversion ID represents a uique customer.

print("Unique Customers with their Customer IDs:\n",df_attribution_results['conversion_id'].unique())
print("Total number of these customers:",df_attribution_results['conversion_id'].nunique())


# In[8]:


#Monthly sessions for may, june, july

mai_sessions=df_attribution_results[df_attribution_results['session_id'].str.contains('2021-05')]
juni_sessions=df_attribution_results[df_attribution_results['session_id'].str.contains('2021-06')]
juli_sessions=df_attribution_results[df_attribution_results['session_id'].str.contains('2021-07')]
juni_sessions.head(10)


# In[9]:


#Group sessions and other details per customer.

grouping_by_customer=pd.pivot_table(df_attribution_results, 
                                    index=['conversion_id','session_id','ihc'])
grouping_by_customer.tail(10)


# In[10]:


#Printing customer data that has specific conditions and values.

ihc_specific_range=grouping_by_customer.query('ihc>= 0.9 | ihc<=0.5') # .mean() can be calculated for all cols
ihc_specific_range.nunique() #total count of findings per phase
ihc_specific_range #finds particular entries with a criteria


# In[11]:


#Finding average of I/H/C of one session to compare the session performences on larger scale 
#to find strongest or weakest sessions
#further avg for all session values for one customer can also be found to compare impact of campaign over them 

print(grouping_by_customer.mean(axis = 1, skipna = True)) #calc avg of all phases

# x = grouping_by_customer[['initializer','closer']].mean(axis=1) #calc avg of specific phases


# In[12]:


#Lets calculate averages for one customer's all the sessions.
#sum is always 1 for all values of all sessions if only one phase is considered.
all_sessions_avg= grouping_by_customer.groupby(['conversion_id'], as_index=False).mean()
all_sessions_avg.tail(4)


# In[13]:


#batch processing

df_attribution_results.head(5)
sliced_attr_result = df_attribution_results.iloc[:30,:]
sliced_attr_result.head(5)
print("Unique customers out of 30 session ids are:\n",sliced_attr_result['conversion_id'].unique(), 
      "\nwith the total count of",sliced_attr_result['conversion_id'].nunique())


# In[14]:


import plotly.express as expr
sesns_per_cust = expr.scatter(sliced_attr_result, x="conversion_id", y="session_id",
                             color_discrete_sequence=['purple'])
sesns_per_cust.update_traces(mode='markers',marker_size= 9)
sesns_per_cust.update_layout(height=700, width=800, title_text="Session Count for each Customer",
                          xaxis_title="Unique Customers", yaxis_title="Number of Sessions")
sesns_per_cust.show()


# In[ ]:





# 3. Visualizing the Data

# In[15]:


#Plotting all customer data, absent bar represents zero value.

import plotly.graph_objects as gph

cid = sliced_attr_result.conversion_id
ihc_col= sliced_attr_result.ihc
initi= sliced_attr_result.initializer
hold= sliced_attr_result.holder
clo= sliced_attr_result.closer

barred_attributions = gph.Figure()
barred_attributions.add_trace(gph.Bar(
    x=cid,
    y=ihc_col,
    name='IHC value',
    marker_color='gold'))
barred_attributions.add_trace(gph.Bar(
    x=cid,
    y=initi,
    name='Initializer Value',
    marker_color='brown'))
barred_attributions.add_trace(gph.Bar(
    x=cid,
    y=hold,
    name='Holder Value',
    marker_color='blue'))
barred_attributions.add_trace(gph.Bar(
    x=cid,
    y=clo,
    name='Closer Value',
    marker_color='red'))

barred_attributions.update_layout(barmode='group', xaxis_tickangle=-30)
barred_attributions.update_layout(xaxis_title="Unique Customers", 
                                  yaxis_title="Values",
                                  title_text="All Scores for Unique Customers")

barred_attributions.show()


# In[16]:


sliced_attr_result2 = df_attribution_results.iloc[30:60,:] #creating second batch of next 30 conversion IDs
sliced_attr_result2.head(5)


# In[17]:


# Plotting IHC Scores of First and Next 30 customers for comparison purposes.
# There can be a difference in number of conversion IDs on x axis because some of them have 0 IHC score.

from plotly.subplots import make_subplots
import plotly.express as expr

cid2 = sliced_attr_result2.conversion_id
ihc_col2= sliced_attr_result2.ihc 

ihc_vs_ihc2 = make_subplots(rows=1, cols=2,
                            subplot_titles=('Batch1 (First 30 Customers)', 'Batch2 (Next 30 Customers)'))

ihc_vs_ihc2.add_trace(gph.Scatter(x=cid, y=ihc_col),row=1, col=1)

ihc_vs_ihc2.add_trace(gph.Scatter(x=cid2, y=ihc_col2), row=1, col=2)
ihc_vs_ihc2.update_layout(xaxis_tickangle=90)
ihc_vs_ihc2.update_layout(height=700, width=800, title_text="Batch1 Vs Batch2 IHC Scores For All Customer Sessions",
                          xaxis_title="X axes- Unique Customers", yaxis_title="Y axes- IHC Score")
ihc_vs_ihc2.update_traces(mode='markers',marker_size= 10)
ihc_vs_ihc2.update_layout(showlegend=False)
ihc_vs_ihc2.show()


# In[18]:


#Calculating mean values for all columns for sake of setting a baseline for comparison and analysis.
mean_IHC_vals= df_attribution_results.groupby('conversion_id', as_index=False).mean()
mean_IHC_vals.head(5)


# In[19]:


#Printing mean values and max of those means separately from original dataset

def phase():
    Initializer_=print("Average value of initializer phase is", 
                       df_attribution_results['initializer'].mean())
    Holder_=print("Average value of holder phase is", df_attribution_results['holder'].mean())
    Closer_=print("Average value of closer phase is", df_attribution_results['closer'].mean())
    print("\nNote: More the value, more of the customers stay in that phase.")
    
    maxwtphase=max(df_attribution_results['initializer'].mean(),
                   df_attribution_results['holder'].mean(),df_attribution_results['closer'].mean())
    print("\nThe maximum of all 3 mean phase values is the",maxwtphase,"for this set of customers.")
phase()    


# In[20]:


#Plotting IHC values as per customers

# import matplotlib.pyplot as plt
# df_scat = pd.DataFrame(mean_IHC_vals,columns=['conversion_id','ihc'])
# df_scat.plot(x ='conversion_id', y='ihc',color= "crimson", kind = 'barh')
# plt.rcParams["figure.figsize"] = (12, 16)
# plt.grid(color="black",axis="x")
# plt.show() #optional method using matplotlib for below method

import plotly.express as expr
covnid_vs_ihc = expr.scatter(mean_IHC_vals, x="ihc", y="conversion_id",
                             color_discrete_sequence=['crimson'], hover_data=['conversion_id'])
covnid_vs_ihc.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gold')
covnid_vs_ihc.update_traces(mode='markers+text',marker_size= 10)
covnid_vs_ihc


# In[21]:


#Plotting all values in one plot for checking overall performance.

import plotly.express as px

alpha= ["initializer","holder","closer"]
beta= mean_IHC_vals
id_vs_IHCvals = px.bar(beta, alpha,orientation="h", hover_name='conversion_id')
id_vs_IHCvals.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
# id_vs_IHCvals.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black')
id_vs_IHCvals.update_layout(xaxis_title="Phase Type", yaxis_title="Customer Index Number")
id_vs_IHCvals.show()


# 4. Playing with IHC Channel Weights

# In[22]:


IHC_wts= pd.read_csv(r"C:\Users\mahaj\Downloads\IHC_channel_weights (1).csv")
IHC_wts


# In[23]:


#Plotting I/H/C weights of all channels as per their index number

# heatmap_channels = px.imshow(IHC_wts,text_auto=True)
# heatmap_channels

axis2=["initializer weight","holder weight","closer weight"]
axis1=IHC_wts
weights_graph = px.line(axis1, axis2, hover_name='channel',
                        color_discrete_sequence=["blue","brown","orange"])
weights_graph.update_traces(mode='markers+lines')
weights_graph.update_layout(xaxis_title="Weight", yaxis_title="Channel Type")
weights_graph.show()


# In[24]:


#finding channels with good, for example,holding performance, assuming >=1 is an indicator of good holder phase 

holder_emphasis=IHC_wts.loc[IHC_wts['holder weight'] > 1]  
holder_emphasis
#holder wt is more means need to focus more on these customers for closing as this phase is doing good 
#bcoz they are in deciding phase, same can be done for other wts


# In[25]:


transition_min_wt_diff=IHC_wts.loc[(IHC_wts['initializer weight'] <1 ) | 
                                   (IHC_wts['holder weight'] <1) | (IHC_wts['closer weight'] <1)]


# In[26]:


#Deriving less effective channels with at least one type of weight less than 1, 
#assuming <1 is an indicator of good holder phase 
#methods with atleast one phase with wt less than 1 which demands more work from marketeers on that phase

less_efficient_methods=IHC_wts.loc[(IHC_wts['initializer weight'] <1 ) | 
                                   (IHC_wts['holder weight'] <1) | (IHC_wts['closer weight'] <1)]
less_efficient_methods


# In[27]:


#Looking for the most efficient channel weight in terms of closing a customer even though I/H phases are shorter

best_channel_phase_closer = IHC_wts['closer weight'].max() 
better_wt= IHC_wts.loc[IHC_wts["closer weight"]==best_channel_phase_closer] 
display("The strongest journey finalization(closer) is",better_wt) 
#more efficient the channel,lesser the demand of focus 


# In[28]:


#Average weights of I/H/C phases and that average distributed over all channels(channel count):

def avgPerformance_distributed():
    
    print("Following 3 distributed averages tell us how much a phase average has contributed in that channel's overall performence: ")
    
    avg_performence_initializer= IHC_wts['initializer weight'].mean()
    Channel_Count= len(IHC_wts.index)
    channelAvg_initializer= avg_performence_initializer/Channel_Count
    print("1. Initialize phase average per channel is",channelAvg_initializer)
    
    avg_performence_holder= IHC_wts['holder weight'].mean()
    channelAvg_holder= avg_performence_holder/Channel_Count
    print("2. Holder phase average per channel is",channelAvg_holder)
    
    avg_performence_closer= IHC_wts['closer weight'].mean()
    channelAvg_closer= avg_performence_closer/Channel_Count
    print("3. Closer phase average per channel is",channelAvg_closer)
    
    max_avg=max(avg_performence_initializer,avg_performence_holder,avg_performence_closer)
    print("\nThe strongest phase performance(average of a phase) in general is",max_avg)    
    
    max_phaseWT= max(channelAvg_initializer,channelAvg_holder,channelAvg_closer)
    print("\nThe maximum average of a phase distributed all over all channels is",max_phaseWT,
          ",\ntells us that phase's contribution in each channel's performance. ")
    
avgPerformance_distributed()


# In[ ]:





# In[ ]:





# Ashutosh Mahajan
