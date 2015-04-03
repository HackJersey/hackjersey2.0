
# coding: utf-8

# In[180]:

import pandas as pd


# In[181]:

salary_data = "oesdata14/oesm14ma/MSA_M2014_dl.xlsx"


# In[182]:

salframe = pd.read_excel(salary_data)


# In[183]:

mystatesframe = salframe[(salframe.PRIM_STATE=='NJ')|(salframe.PRIM_STATE=='PA')|(salframe.PRIM_STATE=='DE')|(salframe.PRIM_STATE=='NY')]


# In[184]:

myalloccframe = mystatesframe[njframe.OCC_TITLE == 'All Occupations']


# In[185]:

njalloccframe=myalloccframe[myallframe['AREA_NAME'].str.contains('NJ')]


# In[186]:

njourframe = njallframe.ix[:,['AREA', 'AREA_NAME', 'TOT_EMP', 'A_MEDIAN']]


# In[187]:

njmsds=njourframe[njourframe.AREA_NAME.str.contains('Division')]
njmsa=njourframe[njourframe['AREA_NAME'].str.endswith('NJ')]


# In[188]:

msa_data = "msacounties.csv"
msd_data = "msdcounties.csv"


# In[189]:

msaframe = pd.read_csv(msa_data, names = ['ID', 'MSA Name', 'FIPS', 'County Name'], skipfooter=2)
msdframe = pd.read_csv(msd_data, names = ['ID', 'MSA Name', 'FIPS', 'County Name'], skipfooter=2)


# In[190]:

msdframe.ID[msdframe.ID==35614]=35644


# In[191]:

joinedmsaframe = pd.merge(njmsa, msaframe, left_on='AREA', right_on='ID', how='inner')


# In[192]:

joinedmsdframe = pd.merge(njmsds, msdframe, left_on='AREA', right_on='ID', how='inner') 


# In[193]:

njmsds = joinedmsdframe[joinedmsdframe['County Name'].str.contains('NJ')]


# In[194]:

njmsas= joinedmsaframe[joinedmsaframe['County Name'].str.contains('NJ')]


# In[195]:

mycounties = njmsds.append(njmsas)


# In[205]:

mediansals = mycounties.ix[:, ['FIPS', 'County Name', 'A_MEDIAN']]
mediansals['County Name']=mediansals['County Name'].map(str.strip)


# In[206]:

mediansals.to_csv('county_median_sals.csv', index=False)


# In[ ]:



