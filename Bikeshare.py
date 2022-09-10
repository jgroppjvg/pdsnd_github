#!/usr/bin/env python
# coding: utf-8

# #1 Popular times of travel (i.e., occurs most often in the start time)
# most common month
# most common day of week
# most common hour of day
#
# #2 Popular stations and trip
# most common start station
# most common end station
# most common trip from start to end (i.e., most frequent combination of start station and end station)
#
# #3 Trip duration
# total travel time
# average travel time
#
# #4 User info
# counts of each user type
# counts of each gender (only available for NYC and Chicago)
# earliest, most recent, most common year of birth (only available for NYC and Chicago)

# In[2]:


import time
import pandas as pd
import numpy as np


# In[5]:


CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # city (chicago, new_york_city, washington)
    # month (all, January, February, March, April, May, June, July, August, September, October, November, December)
    # day of week (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
<<<<<<< HEAD

    city= input('Name of the city to analyze the data: ').lower()
||||||| 043e5f7
       
    city= input('Name of the city to analyze: ').lower()
=======

    city= input('Name of the city to analyze: ').lower()
>>>>>>> refactoring
    month = input('Name of the month to filter by, or "all" to apply no month filter: ').lower().title()
    day = input('Name of the day of week to filter by, or "all" to apply no day filter: ').lower().title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    try:
        df = pd.read_csv(("D://Python GERAL/Udacity/all-project-files/{}").format(CITY_DATA[city]), delimiter=',')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['Month'] = df['Start Time'].dt.strftime('%B')
        df['Day'] = df['Start Time'].dt.strftime('%A')
        df['Hour'] = df['Start Time'].dt.strftime('%H')
        df['Join_Stations']= df[['Start Station','End Station']].apply(lambda x: ' / / '.join(x), axis=1)
    except:
        print('CITY does not exist in the Database, try it again:')
        print('-'*40)
        main()

    if month !=  'All':
        df = df[df['Month']== month]

    if day !=  'All':
        df = df[df['Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    list_key_m = []
    list_value_m = []
    try:
        for key, value in df['Month'].value_counts().items():
            list_key_m.append(key)
            list_value_m.append(value)
        print('The most common Month is {} with {} times'.format(list_key_m[0],list_value_m[0]))
    except:
        print('-'*40)
        print('MONTH does not exist in the Database')
        print('-'*40)
        main()

    # display the most common day of week
    list_key_d = []
    list_value_d = []
    for key, value in df['Day'].value_counts().items():
        list_key_d.append(key)
        list_value_d.append(value)
<<<<<<< HEAD
    print('The most common Day is {} with {} times'.format(list_key_d[0].upper(),list_value_d[0]))

||||||| 043e5f7
    print('The most common Day is {} with {} times'.format(list_key_d[0].upper(),list_value_d[0]))
    
=======
    print('The most common Day is: {} with: {} times'.format(list_key_d[0].upper(),list_value_d[0]))

>>>>>>> refactoring
    # display the most common start hour
    list_key_h = []
    list_value_h = []
    for key, value in df['Hour'].value_counts().items():
        list_key_h.append(key)
        list_value_h.append(value)
    print('The most common Hour is: {} with: {} times'.format(list_key_h[0].upper(),list_value_h[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    list_s_s_name = []
    list_s_s_value = []
    for key, value in df['Start Station'].value_counts().items():
        list_s_s_name.append(key)
        list_s_s_value.append(value)
    print('The most common Start Station is {} with {} times'.format(list_s_s_name[0].upper(),list_s_s_value[0]))

    # display most commonly used end station
    list_e_s_name = []
    list_e_s_value = []
    for key, value in df['End Station'].value_counts().items():
        list_e_s_name.append(key)
        list_e_s_value.append(value)
    print('The most common End Station is {} with {} times'.format(list_e_s_name[0].upper(),list_e_s_value[0]))

    # display most frequent combination of start station and end station trip
    list_s_e_s_name = []
    list_s_e_s_value = []
    for key, value in df['Join_Stations'].value_counts().items():
        list_s_e_s_name.append(key)
        list_s_e_s_value.append(value)
    print('The most common Combination of Station is {} with {} times'.format(list_s_e_s_name[0].upper(),list_s_e_s_value[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    x=df['Trip Duration'].sum()

    # display mean travel time
    y=df['Trip Duration'].mean()

    print('The total travel time is {} minutes with a mean travel time of {} minutes'.format(x,y))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('USER TYPE: ', df['User Type'].value_counts(dropna=False))
    print('-'*40)
    # Display counts of gender
    try:
        print('GENDER: ', df['Gender'].value_counts(dropna=False))
    except:
        print("Don't exist in the Database a column GENDER")

    print('-'*40)
    # Display earliest, most recent, and most common year of birth
    try:
        list_birth_key = []
        list_birth_value = []
        for key, value in df['Birth Year'].value_counts().items():
            list_birth_key.append(key)
            list_birth_value.append(value)
        print('The most common Birth Year is **{}** / / The recent Birth Year is **{}** / / The earliest Birth Year is **{}**'.format(list_birth_key[0],max(list_birth_key),min(list_birth_key)))
    except:
        print("Don't exist in the Database a column BIRTH")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    while (view_data != 'no'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no.\n': ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[9]:


import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # city (chicago, new_york_city, washington)
    # month (all, January, February, March, April, May, June, July, August, September, October, November, December)
    # day of week (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)

    city= str(input('Name of the city to analyze: '))
    month = str(input('Name of the month to filter by, or "all" to apply no month filter: '))
    day = str(input('Name of the day of week to filter by, or "all" to apply no day filter: '))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    try:
        df = pd.read_csv(("D://Python GERAL/Udacity/all-project-files/{}").format(CITY_DATA[city]), delimiter=',')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Month'] = df['Start Time'].dt.strftime('%B')
        df['Day'] = df['Start Time'].dt.strftime('%#A')
        df['Hour'] = df['Start Time'].dt.strftime('%H')
        df['Join_Stations']= df[['Start Station','End Station']].apply(lambda x: ' / / '.join(x), axis=1)
    except:
        print('CITY does not exist in the Database')
        print('-'*40)
        main()

    if month ==  'all':
        df = df[df['Month'] == df['Month']]
    else:
        df = df[df['Month']== month]

    if day ==  'all':
        df = df[df['Day'] == df['Day']]
    else:
        df = df[df['Day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    list_key_m = []
    list_value_m = []
    try:
        for key, value in df['Month'].value_counts().items():
            list_key_m.append(key)
            list_value_m.append(value)
        print('The most common Month is {} with {} times'.format(list_key_m[0],list_value_m[0]))
    except:
        print('-'*40)
        print('MONTH does not exist in the Database')
        print('-'*40)
        main()

    # display the most common day of week
    list_key_d = []
    list_value_d = []
    for key, value in df['Day'].value_counts().items():
        list_key_d.append(key)
        list_value_d.append(value)
    print('The most common Day is {} with {} times'.format(list_key_d[0].upper(),list_value_d[0]))

    # display the most common start hour
    list_key_h = []
    list_value_h = []
    for key, value in df['Hour'].value_counts().items():
        list_key_h.append(key)
        list_value_h.append(value)
    print('The most common Hour is {} with {} times'.format(list_key_h[0].upper(),list_value_h[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    list_s_s_name = []
    list_s_s_value = []
    for key, value in df['Start Station'].value_counts().items():
        list_s_s_name.append(key)
        list_s_s_value.append(value)
    print('The most common Start Station is {} with {} times'.format(list_s_s_name[0].upper(),list_s_s_value[0]))

    # display most commonly used end station
    list_e_s_name = []
    list_e_s_value = []
    for key, value in df['End Station'].value_counts().items():
        list_e_s_name.append(key)
        list_e_s_value.append(value)
    print('The most common End Station is {} with {} times'.format(list_e_s_name[0].upper(),list_e_s_value[0]))

    # display most frequent combination of start station and end station trip
    list_s_e_s_name = []
    list_s_e_s_value = []
    for key, value in df['Join_Stations'].value_counts().items():
        list_s_e_s_name.append(key)
        list_s_e_s_value.append(value)
    print('The most common Combination of Station is {} with {} times'.format(list_s_e_s_name[0].upper(),list_s_e_s_value[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    x=df['Trip Duration'].sum()

    # display mean travel time
    y=df['Trip Duration'].mean()

    print('The total travel time is {} minutes with a mean travel time of {} minutes'.format(x,y))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('USER TYPE: ', df['User Type'].value_counts(dropna=False))
    print('-'*40)
    # Display counts of gender
    try:
        print('GENDER: ', df['Gender'].value_counts(dropna=False))
    except:
        print("Don't exist in the Database a column GENDER")

    print('-'*40)
    # Display earliest, most recent, and most common year of birth
    try:
        list_birth_key = []
        list_birth_value = []
        for key, value in df['Birth Year'].value_counts().items():
            list_birth_key.append(key)
            list_birth_value.append(value)
        print('The most common Birth Year is **{}** / / The recent Birth Year is **{}** / / The earliest Birth Year is **{}**'.format(list_birth_key[0],max(list_birth_key),min(list_birth_key)))
    except:
        print("Don't exist in the Database a column BIRTH")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print(df.head(5))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:
