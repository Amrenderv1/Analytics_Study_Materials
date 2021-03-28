#!/usr/bin/env python
# coding: utf-8

# In[45]:


import os
path='E:\Arise_betsol\DATA'
os.chdir(path)


# In[46]:


import pandas as pd


# In[47]:


df=pd.read_excel('Stacked_Ranking_Data_Retention.xlsx')


# In[48]:


df.head()


# In[49]:


df.isnull().sum()


# In[50]:


df.info


# In[51]:


df1=df[['NPS %','TSR %','AHT','Monthly CA %']]
df2=df[['CSP ID','CSP Name','Wave']]


# In[52]:


def normalize(df):
    result=df.copy()
    for colname in df.columns:
        max_value=df[colname].max()
        min_value=df[colname].min()
        result[colname]=(df[colname]-min_value)/(max_value-min_value)
    return result
        


# In[53]:


data_normalize=normalize(df1)
data_final=pd.concat([df2,data_normalize],axis=1)
data_final


# In[54]:


df.groupby('CSP ID')


# In[55]:


#kpi importance


AHT 20%
NPS 40%
CA 20%
TSR 20%


# In[56]:


data_final['AHT_']=data_final['AHT'].apply(lambda x: x*0.2)
data_final['NPS %_']=data_final['NPS %'].apply(lambda x: x*0.4)
data_final['TSR %_']=data_final['TSR %'].apply(lambda x: x*0.2)
data_final['Monthly CA %_']=data_final['Monthly CA %'].apply(lambda x: x*0.2)
data_final['Total_Point']=data_final['AHT_']+data_final['NPS %_']+data_final['TSR %_']+data_final['Monthly CA %_']
data_final['Z_score']=(data_final['Total_Point']-data_final['Total_Point'].mean())/data_final['Total_Point'].std()


# In[57]:


data_final.sort_values(['Z_score'],axis=0,ascending=False ,inplace=True)


# In[58]:


data_final


# In[59]:


data_final.reset_index(inplace = True, drop = True)


# In[60]:


data_final


# In[61]:


data_final['Z_score_Rank'] = data_final['Z_score'].rank(ascending = False) 
  


# In[62]:


data_final.head(209)


# In[84]:


writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')


# In[89]:


data_final.to_excel(writer, sheet_name='Sheet1')


# In[86]:


writer.save()


# In[92]:


data_final.to_excel (r'E:\Arise_betsol\DATA\August_Ned_Retention.xlsx',sheet_name='kpi_data', index = False)
#data_final.to_excel(r'filename',sheet_name='kpi_data',index=False)


# ## NOTE: NPS % ,TSR % ,AHT,Monthly CA % are the normalize values
# 
# ## AHT_	NPS %_	TSR %_	Monthly CA %_ are the values after applying KPI Weightage
# 
# ## KPI Weightage 
# ## 20 % FOR AHT ,TSR ,Monthly CA %
# ## 40 % FOR NPS
# 

# In[ ]:





# In[ ]:





# In[ ]:




