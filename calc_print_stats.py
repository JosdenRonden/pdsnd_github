import time
import pandas as pd

def time_stats(df, month, weekday):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # add hour column to the dataframe
    df['hour']     = df['Start Time'].dt.hour

    # I added a month-weekday-hour column to the data frame,
    # needed to get the  busiest moment on a day
    # (the busiest month, busiest weekday, busiest hour is not necessarily the busiest moment,
    # for example, for washington, month April, all weekdays, Sunday is the most common day,
    # 5 the most common hour, but the busiest moment is Wednesday, 7 o'clock )

    # https://datatofish.com/concatenate-values-python/
    df['mo_wd_hr'] = df['month'] + "-" + df['weekday'] + "-" + df['hour'].map(str)

    # collect statistics about most popular times in a list
    most_pop_times = []
    windows        = ['month', 'weekday', 'hour', 'mo_wd_hr']
    for window in windows:
        m = df[window].mode()[0]
        c = df[df[window] == m][window].count()
        most_pop_times.append (m)
        most_pop_times.append (c)
    if month == "All":
        print("Most common month:   ", most_pop_times [0], "  Count: ", most_pop_times [1])

    if weekday == "All":
        print("Most common weekday: ", most_pop_times [2], "  Count: ", most_pop_times [3])

    print("Most common hour:    ", most_pop_times [4], "  Count: ", most_pop_times [5])
    print("Busiest moment:      ", most_pop_times [6], "  Count: ", most_pop_times [7], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # collect statistics about most common stations in a list
    most_pop_station = []
    df['Start_End_Station'] =  'FROM: ' + df['Start Station'] + "   TO: " + df['End Station']
    windows  = ['Start Station', 'End Station', 'Start_End_Station']
    for window in windows:
        m = df[window].mode()[0]
        c = df[df[window] == m][window].count()
        most_pop_station.append (m)
        most_pop_station.append (c)

    print("Most common start station: ", most_pop_station [0], "   Count: ", most_pop_station [1])
    print("Most common end station:   ", most_pop_station [2], "   Count: ", most_pop_station [3])
    print("Most common trip:          ", most_pop_station [4], "   Count: ", most_pop_station [5], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # collect statistics about trip duration in a list
    trip_duration = []
    trip_duration.append(df['Trip Duration'].sum() / (60*60*24))
    trip_duration.append(df['Trip Duration'].mean() / (60*60))
    trip_duration.append(df['Trip Duration'].count())

    # string formatting
    # https://mkaz.blog/code/python-string-format-cookbook/
    print("Total travel time (weekdays):     {:.1f}".format(trip_duration  [0]))
    print("Average travel time (hours): {:.1f}\n".format(trip_duration  [1]))
    print("Count: {:.0f}\n".format(trip_duration  [2]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # replace nan's
    # https://stackoverflow.com/questions/53609016/how-to-replace-nan-value-in-python
    df['User Type'].fillna('Unknown', inplace=True)

    # produce a report (without too much unnecessary info such as data types)
    # https://stackoverflow.com/questions/40581312/how-to-create-a-frequency-table-in-pandas-python
    df_user_type = pd.value_counts(df['User Type']).to_frame().sort_index()
    df_user_type.columns = ['Count']
    print("Counts of each user type:\n", df_user_type, "\n")

    # display counts of gender; display earliest, most recent, and most common year of birth
    if city != "Washington":
        df['Gender'].fillna('Unknown', inplace=True)
        df_gender = pd.value_counts(df['Gender']).to_frame().sort_index()
        df_gender.columns = ['Count']
        print("Counts of each gender:\n", df_gender, "\n")

        yob = []
        yob.append(df['Birth Year'].min())
        yob.append(df['Birth Year'].max())
        yob.append(df['Birth Year'].mode()[0])
        print("Earliest, most recent, most common year of birth: {:.0f}, {:.0f}, and {:.0f}".format(yob[0], yob[1], yob[2]))
    else:
        print("Sorry, for Washington, no data available for gender and birth year\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def calc_print_stats (df, city, month, weekday):
    '''
    calculates requested statistics
    '''
    print("\nTHE RESULTS FOR CITY: {}, MONTH: {}, WEEKDAY: {}".format (city.upper(), month.upper(), weekday.upper()))
    time_stats(df, month, weekday)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df, city)
