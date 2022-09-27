#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import random

###################################
def random_date(after, before):
    start_u = after.value//10**9
    end_u = before.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, 1), unit='s')[0]

def random_dates(after, before, number):
    start_u = after.value//10**9
    end_u = before.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, number), unit='s')

def dateTime_to_string(column):
    work = []
    for i in column: work.append( i.strftime('%Y-%m-%d %H:%M:%S.000') )
    return work 

def random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))
    
def random_uuid():
    work = random_string(8) + '-' + random_string(4) + '-' + random_string(4) + '-' + random_string(4) + '-' + random_string(12)
    return work

def random_city_id():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(3))

def synthetise_dispatches(row_number=1000):
    # File headers:
    #   start_timestamp_utc,end_timestamp_utc,start_timestamp_local,
    #   end_timestamp_local,driver_uuid,city_id,minutes_online,minutes_active,
    #   dispatches,rejections,accepts,expireds,driver_cancellations,rider_cancellations,
    #   completed_trips,trip_fares,driver_adjusted_fares,flow_type,partner_uuids,vehicle_uuids,minutes_on_trip    

    after_date  = pd.to_datetime('2020-01-01')
    before_date = pd.to_datetime('2022-01-01')
    locate_time_difference = 1      # one hour time difference between UTC and Geneva

    # populate start_timestamp_utc
    dispatches_df = pd.DataFrame()
    dispatches_df['start_timestamp_utc'] = random_dates(after_date, before_date, row_number)
    dispatches_df = dispatches_df.sort_values(by='start_timestamp_utc',ascending=True)
    dispatches_df = dispatches_df.reset_index(drop=True)
    #dispatches_df['start_timestamp_utc'] = dispatches_df['start_timestamp_utc'].strftime('%Y-%m-%d %H:%M:%S.000')
    
    # populate end_timestamp_utc: must be after start_timestamp_utc of the same row, but before start_timestamp_utc of the next row
    end_timestamps_utc = []
    row_iterator = dispatches_df.iterrows()
    _, last = next(row_iterator)
    for i, row in row_iterator:
        end_timestamps_utc.append( random_date( last['start_timestamp_utc'], row['start_timestamp_utc'] ) )
        last = row
    end_timestamps_utc.append( random_date( last['start_timestamp_utc'], before_date ) )
    dispatches_df['end_timestamp_utc'] = end_timestamps_utc
    
    # add time zones
    dispatches_df['start_timestamp_local'] = dispatches_df['start_timestamp_utc'] + pd.DateOffset(hours=locate_time_difference)
    dispatches_df['end_timestamp_local'] = dispatches_df['end_timestamp_utc'] + pd.DateOffset(hours=locate_time_difference)
    
    # pre-compute minutes_online
    minutes_online_list = dispatches_df['end_timestamp_local'] - dispatches_df['start_timestamp_local']
    
    # convert datetimes to string (now that we are done with time-sensitive operations)
    datetime_rows = ['start_timestamp_utc','end_timestamp_utc','start_timestamp_local', 'end_timestamp_local']
    for datetime_row in datetime_rows: dispatches_df[datetime_row] = dateTime_to_string(dispatches_df[datetime_row])
    
    # populate various codes
    dispatches_df['driver_uuid'] = random_uuid()
    dispatches_df['city_id']     = random_city_id()
    dispatches_df['minutes_online'] = minutes_online_list / pd.Timedelta(minutes=1)
    dispatches_df['minutes_active'] =         0
    dispatches_df['dispatches'] =             0
    dispatches_df['rejections'] =             0
    dispatches_df['accepts'] =                0
    dispatches_df['expireds'] =               0
    dispatches_df['driver_cancellations'] =   0
    dispatches_df['rider_cancellations'] =    0
    dispatches_df['completed_trips'] =        0
    dispatches_df['trip_fares'] =             0
    dispatches_df['driver_adjusted_fares'] =  0
    dispatches_df['flow_type'] =              'UberX'
    dispatches_df['partner_uuids'] =          '"[""'+ random_uuid() +'""]"'
    dispatches_df['vehicle_uuids'] =          '"[""'+ random_uuid() +'""]"'
    dispatches_df['minutes_on_trip'] = 0

    return dispatches_df

###############################
dispatches_df = synthetise_dispatches(9000)

print(dispatches_df)
dispatches_df.to_csv('synthetic_Uber_data/08 - Driver Dispatches Offered and Accepted.csv', index=False)
        
