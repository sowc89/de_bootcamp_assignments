#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import datetime


# In[5]:


# Read a sample of the data
prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
df_trip_data = pd.read_parquet(prefix + 'green_tripdata_2025-11.parquet')

taxi_zone_data = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
df_zone_data = pd.read_csv(taxi_zone_data)


# In[15]:


df_trip_data.head()


# In[21]:


# November trips less than a mile
nov_trip_lt_1_mile = df[(df['lpep_pickup_datetime'] >= '2025-11-01') & (df['lpep_pickup_datetime'] < '2025-12-01') & (df['trip_distance'] <= 1)]

len(nov_trip_lt_1_mile)


# In[25]:


# Date of longest trip where trip distance is less than 100 miles
trips_lt_100_miles = df[(df['trip_distance'] < 100)]

longest_trip_id = trips_lt_100_miles['trip_distance'].idxmax()

row_longest_trip = trips_lt_100_miles.loc[longest_trip_id]

row_longest_trip['lpep_pickup_datetime']


# In[45]:


# Pickup zone with largest total amount on Novemeber 18th

nov_18_trips = df[df['lpep_pickup_datetime'].dt.date == datetime.date(2025, 11, 18)]
nov_18_trips_with_zones = pd.merge(nov_18_trips, df_zone_data, left_on = 'PULocationID', right_on = 'LocationID', how= 'inner')


# In[42]:


nov_18_trip_zones_total_amt = nov_18_trips_with_zones.groupby('Zone', as_index=False)['total_amount'].sum()
zone_with_highest_total_amt_nov_18 = nov_18_trip_zones_total_amt[nov_18_trip_zones_total_amt['total_amount'] == nov_18_trip_zones_total_amt['total_amount'].max()]


# In[55]:


# Novemeber trips and pickup Zone: East Harlem North - Drop off zone with max tip amount

nov_trips = df[(df['lpep_pickup_datetime'] >= '2025-11-01') & (df['lpep_pickup_datetime'] < '2025-12-01')]
nov_trips_with_zones = pd.merge(nov_trips, df_zone_data, left_on = 'PULocationID', right_on = 'LocationID', how= 'inner')
nov_trips_pickup_EHN = nov_trips_with_zones[nov_trips_with_zones['Zone'] == 'East Harlem North']

nov_trips_pickup_EHN_max_tip_id = nov_trips_pickup_EHN['tip_amount'].idxmax()

row_w_max_tip = nov_trips_pickup_EHN.loc[nov_trips_pickup_EHN_max_tip_id]

drop_zone_w__max_tip =  df_zone_data[ df_zone_data['LocationID'] == row_w_max_tip['DOLocationID'] ]

drop_off_zone_name = drop_zone_w__max_tip['Zone']

drop_off_zone_name


# In[ ]:




