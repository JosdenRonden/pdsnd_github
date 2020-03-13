import pandas as pd
import numpy as np

def load_data (city, month, weekday, city_data):
    
    df = pd.read_csv(city_data [city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract the month name out of a datatime 
    # https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967
    # note: there is a "weekday_name" function, but I could not find "month_name" function
    # get first three letters of a series of type string
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.slice.html
    df['month']   = df['Start Time'].dt.strftime('%B').str.slice(stop=3) 
    df['weekday'] = df['Start Time'].dt.weekday_name.str.slice(stop=3)


    if month != "All":
        df = df[df['month'] == month]
    if weekday != "All":
        df = df[df['weekday'] == weekday]
        
    return df