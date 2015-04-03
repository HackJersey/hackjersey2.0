
# coding: utf-8

# In[164]:

import json
import pandas as pd


# In[51]:

active_pensions = "active_pensions.csv"


# In[52]:

apframe = pd.read_csv(active_pensions)


# In[80]:

apframe.MEMBER_MI=apframe.MEMBER_MI.fillna(value='none')
apframe.MEMBER_LAST_NAME = apframe.MEMBER_LAST_NAME.fillna(value='none')
apframe.MEMBER_FIRST_NAME = apframe.MEMBER_FIRST_NAME.fillna(value='none')
apframe.ALL_EMPLOYERS_SALARY_AMT=apframe.ALL_EMPLOYERS_SALARY_AMT.apply(lambda x: float(x[1:]))


# In[81]:

deduped = apframe.drop_duplicates(['MEMBER_LAST_NAME', 'MEMBER_FIRST_NAME', 'MEMBER_MI', 'BIRTH_YEAR'])


# In[82]:

statewide = 'deduped[deduped.LOCATION_NAME==STATEWIDE']


# In[83]:

state_median = statewide.ALL_EMPLOYERS_SALARY_AMT.median()


# In[87]:

rest = apframe[apframe.LOCATION_NAME!="STATEWIDE"]


# In[159]:

counties = rest.LOCATION_NAME.unique()
data_list = {}


# In[160]:

county_meds = "county_median_sals.csv"
overall_medians = pd.read_csv(county_meds, dtype={'FIPS':'str'})


# In[161]:

combined=pd.merge(rest, overall_medians, left_on="LOCATION_NAME", right_on="County Name", how="left")


# In[162]:

for county in counties:
    if county=='REGIONAL':
        pass
    else:
        FIPS = combined.FIPS[combined.LOCATION_NAME==county].unique()[0]
        county_dict={}
        this_county = combined[combined.LOCATION_NAME==county]
        teachers = this_county[this_county.PENSION_FUND_ID==1]
        public = this_county[this_county.PENSION_FUND_ID==2]
        copsfire = this_county[this_county.PENSION_FUND_ID==3]
        teach_med = teachers.ALL_EMPLOYERS_SALARY_AMT.median()
        public_med = public.ALL_EMPLOYERS_SALARY_AMT.median()
        cops_med = copsfire[copsfire.PENSION_GROUP_ID==1].ALL_EMPLOYERS_SALARY_AMT.median()
        fire_med = copsfire[copsfire.PENSION_GROUP_ID==2].ALL_EMPLOYERS_SALARY_AMT.median()
        overall=this_county.A_MEDIAN.unique()
        county_dict['OVERALL']=overall[0]
        county_dict['COUNTY']=county
        county_dict['STATEWIDE']=state_median
        county_dict['PUBLIC_EMPLOYEES']=public_med
        county_dict['TEACHERS']=teach_med
        county_dict['POLICE']=cops_med
        county_dict['FIRE']=fire_med
        data_list[FIPS]=county_dict


# In[169]:

my_json="data.json"

with open(my_json, "wb") as j:
    json.dump(data_list, j)


# In[ ]:



