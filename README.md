# Bikeshare Data Analysis
In this project, I analyze bikeshare data using a python terminal code to query a database.

## Installation Instructions
In order to use this code, you will need to install the following Python Libraries:
```python
import time
import pandas as pd
import numpy as np
```
In addition, you will have to download the three datasets *"chicago.csv"*, *"washington.csv"* and *"new_york_city.csv"*.

These databases should contain at least the following variables and data types:

1. Start Time as timestamp
2. End Time as timestamp
3. Trip Duration as integer
4. Start Station as string
5. End Station as string
6. User Type as string
7. Gender as string
8. Birth Year as integer

## Functions

There are several functions along the code:

```python
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
 def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
 def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
 def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
```

## Limitations

The presented code is limited to databases structured as presented in the previous sections. 

