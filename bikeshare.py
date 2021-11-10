"""
# Statistic Computed

#1 Popular times of travel (i.e., occurs most often in the start time)

    most common month
    most common day of week
    most common hour of day

#2 Popular stations and trip

    most common start station
    most common end station
    most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

    total travel time
    average travel time

#4 User info

    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)

"""



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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (input('Enter city (chicago, new york city, washington): ')).lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('wrong input')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = (input('Enter month (all,january,february,...,june): ')).lower()
      if month in ['all', 'january','february','march','april','may','june']:
          break
      else:
          print('wrong input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = (input('Enter month (all, monday, tuesday, ... sunday): ')).lower()
      if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        break
      else:
          print('wrong input')

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

    #load data
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # return df
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]
    

    # TO DO: display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_freq_hour = df['hour'].mode()[0]
    

    print('Most common month is the {}th month'.format(most_freq_month))
    print('Most common day of week is {}'.format(most_freq_day))
    print('Most common start hour is {}'.format(most_freq_hour))

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combine_station = df[['Start Station','End Station']].apply(tuple, 1).mode()[0]
    print('\nMost frequent combination of start and end station trip is {} and {}'.format(popular_combine_station[0],popular_combine_station[1]))

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
 
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    print('Total travel time: {} seconds'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: {} seconds'.format(round(mean_travel_time,1)))

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
    
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('**** User Types ****')
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
      gender = df['Gender'].value_counts()
      print('\n**** Gender ****')
      print(gender)


      # TO DO: Display earliest, most recent, and most common year of birth
      earliest = df['Birth Year'].min()
      print('\nEarliest year of birth: {}'.format(int(earliest)))

      most_recent = df['Birth Year'].max()
      print('Most recent year of birth: {}'.format(int(most_recent)))

      most_common = df['Birth Year'].mode()[0]
      print('Most common year of birth: {}'.format(int(most_common)))


    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)

    
def display_raw_data(df):
    """
    Ask user whether they would like to see the raw data. If the user answers 'yes,' 
    then it returns 5 rows of the data at a time, and again ask the user if they would like to see 5 more rows of the data. 
    This continue prompting and printing the next 5 rows at a time until the user chooses 'no'.
  
    """ 
    raw = (input("Would you like to view data format (yes/no)").lower())# TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)
    i=0
    while True:
      if raw == 'no':
        break
      elif raw == 'yes':
          print(df.iloc[i:i+5,:]) # TO DO: appropriately subset/slice your dataframe to display next five rows
          raw = (input("Do you like to view more rows? (yes/no)")).lower() # TO DO: convert the user input to lower case using lower() function
          i+=5
      else:
          raw = (input("\nYour input is invalid. Please enter only 'yes' or 'no'\n")).lower()

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
