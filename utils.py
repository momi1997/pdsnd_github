"""This file contains helper functions that can process
data and prepare it for the functions that will generate
the UI """
import pandas as pd
import time


CITY_DATA = { 'CHI': 'chicago.csv',
              'NYC': 'new_york_city.csv',
              'WA': 'washington.csv' }

NOT_AVAILABLE = "Not available"



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() #weekday_name was deprecated


    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == int(month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    
    return df



def time_stats(df):
    """
    Calculates statistics on the most frequent times of travel.

    Args:
        (pandas.DataFrame) df - the dataframe that represents filtered city data
    Returns:
        (tuple) a tuple containing:
            (str) most_common_month - the most common month name (June, July...)
            (str) most_common_dayofweek - the most common day of week name (Saturday, Sunday...)
            (int) most_common_hour - the most common hour (8, 13...)
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # calculates the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[df["month"].value_counts().idxmax() - 1]

    # calculates the most common day of week
    most_common_dayofweek = df["day_of_week"].value_counts().idxmax()

    # calculates the most common start hour
    # Gets a Series of hours from the Start Time column of the Dataframe
    hours = pd.to_datetime(df['Start Time']).dt.hour
    # Gets the most common hour in the hours Series
    most_common_hour = hours.value_counts().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 

    return most_common_month, most_common_dayofweek, most_common_hour


def station_stats(df):
    """
    Calculates statistics on the most popular stations and trip.

    Args:
        (pandas.DataFrame) df - the dataframe that represents filtered city data
    Returns:
        (tuple) a tuple containing:
            (str) most_common_start_station - the most common start station
            (str) most_common_end_station - the most common end station
            (tuple) most_common_combination - the most common combination of start and end stations
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # calculates most commonly used start station
    most_common_start_station = df["Start Station"].value_counts().idxmax()

    # calculates most commonly used end station
    most_common_end_station = df["End Station"].value_counts().idxmax()

    # calculates most frequent combination of start station and end station trip
    most_common_combination = str(df.groupby(["Start Station","End Station"]).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return (most_common_start_station, most_common_end_station,
            most_common_combination)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculates total travel time
    total_travel_time = df["Trip Duration"].sum()

    # calculates mean travel time
    mean_travel_time = df["Trip Duration"].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return total_travel_time, mean_travel_time




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # calculates counts of user types
    types_count = df["User Type"].value_counts().to_string()

    # calculates  counts of gender
    gender_count = NOT_AVAILABLE
    # Checks if there's a gender column in the dataframe
    # If it's the case we calculate the gender count
    # otherwise we return "Not available"
    if "Gender" in df.columns:
        gender_count = df["Gender"].value_counts().to_string()

    # calculates earliest, most recent, and most common year of birth
    earliest_year = NOT_AVAILABLE
    most_recent_year = NOT_AVAILABLE
    most_common_year = NOT_AVAILABLE
    
    if "Birth Year" in df.columns:
        # Gets the earliest year of birth
        earliest_year = df["Birth Year"].min()
        # Gets the most recent year of birth
        most_recent_year = df["Birth Year"].max()
        # Gets the most common year of birth
        most_common_year = df["Birth Year"].mode().to_string(index=False)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return [str(types_count), str(gender_count), str(earliest_year),
            str(most_recent_year), str(most_common_year)]


            