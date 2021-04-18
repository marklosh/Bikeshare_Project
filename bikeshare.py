import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }

def prompt_user_to_enter_filter():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello, Hope you are doing fine! Let\'s explore some US bikeshare data!'.center(80, "="))
    # get user input for city (chicago, new york city, washington). HINT: Used a while loop to handle invalid inputs
    while True:

        city = input("Choose a city you wanna analyze its data \nAvailable cities include:\n 1]Chicago\n 2]New York City\n 3]Washington!\n ").lower()
        print()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break



     # get user input for month (all, january, february, ... , june)
    month = None
    month_filter = ['all', 'january', 'february', 'march',
                    'april', 'may', 'june']
    while month not in month_filter:
        print("kindly enter the month which you want to analyze data by \n")
        month = input("\nFilter data by month\n[ all, january, february,"
                      "march, april, may, or june ] : ").lower()
        print()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    day_filter = ['all', 'sunday', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday']
    while day not in day_filter:
        print("kindly enter the day which you want to analyze data by \n")
        day = input("\nFilter data by day of the week\n['all', "
                    "'sunday', 'monday', ...., 'saturday'] : ").lower()
        print()
    print("YOUR INPUTS".center(80, "="))
    print("CITY CATEGORY\nYou selected : \n", city)
    print("MONTH CATEGORY\nYou selected : \n", month)
    print("DAY CATEGORY\nYou selected : \n", day)
    print('-'*80, '\n')
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
    #load_data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month from Start Time and create new column month
    df['month'] = df['Start Time'].dt.month

    #extract day name from Start Time and create new column day_of_week
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #case1: filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1

        #creating a new DataFrame based on selected filter criteria(month)
        df = df[df['month'] == month]
    #case2: filter by day if applicable
    if day != 'all':
        #creating a new DataFrame based on selected filter criteria(day)
        df = df[df['day_of_week'] == day.title()]

    return df

def time_statistics(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel\n'.center(80, "="))
    start_time = time.time()

    # display the most common month
    # extract month from the Start Time column to create month column
    df['month'] = df['Start Time'].dt.month
    #find the most common month of all
    common_month = df['month'].mode()[0]
    print("the most frequent month of travel is .... ", common_month)


    # display the most common day of week
    # extract day of the week from the Start Time column to create day_of_week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #find the most common day of the week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("the most frequent day of travel is .... ", common_day_of_week)

    # display the most common start hour
    # extract hour from the Start Time column to create common_hour column
    df['hour'] = df['Start Time'].dt.hour
    #display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("the most frequent hour of travel is .... ", common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80, "\n")

def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if 'Start Station' in df.columns:
        common_start = df['Start Station'].mode()[0]
        print("most commonly used start station is .... ", common_start)

    # display most commonly used end station
    if 'End Station' in df.columns:
        common_end = df['End Station'].mode()[0]
        print("most commonly used start station is .... ", common_end)

    # display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        df['route'] = df['Start Station'] + ' to ' + df['End Station']
        popular_route = df['route'].mode()[0]
        print("most frequently used route is .... ",popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def trip_duration_statistics(df):
    """Displays statistics on the total and average trip duration."""

    print()
    if 'Trip Duration' in df.columns:
        print(' Calculating Trip Duration '.center(78, '='))
        start_time = time.time()

    #Trip duration statistics;
    #case1: maximum travel time
    print("Maximum travel time is .... ", df['Trip Duration'].max())
    #case2: minimum travel time
    print("Minimum travel time is .... ", df['Trip Duration'].min())
    #case3; most popular travel time
    print("Most popular travel time is .... ", df['Trip Duration'].mode()[0])
    #case4: minimum travel time
    print("Average travel time is .... ", df['Trip Duration'].mean())
    #case5: minimum travel time
    print("Total travel time is .... ", df['Trip Duration'].sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80, '\n')

def user_details(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User details...\n')
    start_time = time.time()

    # Display counts of user types
    print("USER STATS".center(80, "="))
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        print("GENDER STATS".center(80, "="))
        df['Gender'].replace(np.nan, 'not disclosed', inplace=True)
        print(df['Gender'].value_counts(dropna=False))


    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        born_earliest = df['Birth_Year'].min()
        print(born_earliest)
        born_most_recent = df['Birth_Year'].max()
        print(recent)
        most_common_birth_yr = df['Birth Year'].mode()[0]
        print(most_common_birth_yr)
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

#Asking 5 lines of the raw data and more from the user, if they want
def data(df):
    raw_data = 0
    choices = ["yes", "no"]
    while True:
        choice = input("Do you want to see the raw data? Yes or No").lower()
        if choice not in choices:
            choice = input("You wrote the wrong word. Please type Yes or No.").lower()
        elif choice == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No").lower()
            if again == 'no':
                break
        elif choice == 'no':
            return

def main():
    while True:
        city, month, day = prompt_user_to_enter_filter()
        df = load_data(city, month, day)

        time_statistics(df)
        station_statistics(df)
        trip_duration_statistics(df)
        user_details(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
