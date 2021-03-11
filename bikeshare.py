import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Greetings Mr. Hoffman! It seems that our new biking service is doing great!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_check = 0

    while city_check == 0:

    	city = input("Please select a city between Chicago, New York City and Washington.")

    	if (str(city) != 'Chicago') and (str(city) != 'New York City') and (str(city) != 'Washington'):

    		print(str(city))

    		print('Please try again. I need you to use the exact words I typed before!')

    	else:
    		city_check = 1

    # get user input for month (all, january, february, ... , june)

    month_check = 0
    L_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'all']

    while month_check == 0:

    	month = input("Please select a month between Jan, Feb, Mar, Apr, May, Jun or all.")

    	if str(month) not in L_month:

    		print('Please try again. I need you to use the exact words I typed before!')

    	else:
    		month_check = 1


    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_check = 0
    L_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'all']

    while day_check == 0:

    	day = input("Please select a day between Mon, Tue, Wed, Thu, Fri, Sat, Sun or all.")

    	if str(day) not in L_day:

    		print('Please try again. I need you to use the exact words I typed before!')

    	else:
    		day_check = 1


    print('-'*40)
    return city, month, day


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

    if str(city) == 'Chicago':
    	df = pd.read_csv('chicago.csv', sep=',', na_values='-', encoding='utf-8')

    elif str(city) == 'New York City':
    	df = pd.read_csv('new_york_city.csv', sep=',', na_values='-', encoding='utf-8')

    else:
    	df = pd.read_csv('washington.csv', sep=',', na_values='-', encoding='utf-8')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    ###Apply filter by month: Jan, Feb, Mar, Apr, May, Jun

    if str(month) != 'all':

    	L_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

    	for m in range(len(L_month)):

    		if str(L_month[m]) == str(month):

    			df = df.loc[df['Start Time'].dt.month == (m + 1)]


    ###Apply filter by day: Mon, Tue, Wed, Thu, Fri, Sat, Sun

    if str(day) != 'all':

    	L_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    	for d in range(len(L_day)):

    		if str(L_day[d]) == str(day):

    			df = df.loc[df['Start Time'].dt.dayofweek == (d)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month

    result_month = df['Start Time'].dt.month

    result_month = int(result_month.mode()[0])

    L_month = ['January', 'February', 'March', 'April', 'May', 'June']

    print("Got it! The most common month is... {}!".format(L_month[result_month - 1]))

    # display the most common day of week

    result_day = df['Start Time'].dt.dayofweek

    result_day = int(result_day.mode())

    L_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    print("Alright! The most common day of the week is... {}!".format(L_day[result_day]))

    # display the most common start hour

    result_hour = df['Start Time'].dt.hour

    result_hour = int(result_hour.mode())

    print("OK! The most common hour is... {}:00!".format(result_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    result_start_station = str(df['Start Station'].mode()[0])

    print("This is a good one! The most common start station is... {}!".format(result_start_station))

    # display most commonly used end station

    result_end_station = str(df['End Station'].mode()[0])

    print("And the most common end station is... {}!".format(result_end_station))

    # display most frequent combination of start station and end station trip

    result_OD = (df['Start Station'].map(str) + ' - ' + df['End Station'].map(str)).mode()[0]

    print("Hold on! The most O-D pair is... {}!".format(result_OD))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = int(df['Trip Duration'].sum())

    # Convert to hours

    total_travel_time = total_travel_time/3600

    print("Wow! The total travel time is... {:,.2f} hours!".format(total_travel_time))

    # display mean travel time

    mean_travel_time = float(df['Trip Duration'].mean())

    # Convert to minutes

    mean_travel_time = mean_travel_time/60

    print("And the mean travel time is... {:,.2f} minutes!".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    c_user_types = df['User Type'].value_counts()

    print("These are the amount of subscribers and customers: \n")
    print(c_user_types)

    # Display counts of gender

    if (str(city) == 'Chicago') or (str(city) == 'New York City'):

    	c_user_gender = df.loc[df['User Type'] == 'Subscriber']
    	c_user_gender = df['Gender'].value_counts()

    	print("This is counts of gender of {}: \n".format(str(city)))
    	print(c_user_gender)

    else:
    	print("Sorry! There's no gender info in {}!".format(str(city)))

    # Display earliest, most recent, and most common year of birth

    if (str(city) == 'Chicago') or (str(city) == 'New York City'):

    	df_ages = df.loc[df['User Type'] == 'Subscriber']
    	old_year = int(df_ages['Birth Year'].min())
    	young_year = int(df_ages['Birth Year'].max())
    	popular_year = int(df_ages['Birth Year'].mode())

    	print("The oldest subscriber was born on {}!".format(str(old_year)))
    	print("The youngest subscriber was born on {}!".format(str(young_year)))
    	print("The most common birth year is {}!".format(str(popular_year)))

    else:
    	print("Sorry! There's no year of birth info in {}!".format(str(city)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

    	#Get inputs for data reading and filters
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Get statistics

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        #Ask for data rows

        individual_data = input('\nWould you like to check 5 lines of individual trip data? Please type yes or no.\n')

        n = 5
        m = 0

        while (individual_data.lower() == 'yes'):

        	if int(n) < int(df.shape[0]):

	        	print(df.iloc[m:n, :])
	        	n += 5
	        	m += 5

	        	individual_data = input('\nWould you like to 5 lines of check individual trip data? Please type yes or no.\n')

	        else:

	        	individual_data = 'no'
	        	print('Sorry! There\'s no more data to show!')

        #Ask for restarting the program

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
