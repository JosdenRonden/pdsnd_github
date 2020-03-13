import time
from get_filters import get_filters
from load_data import load_data
from calc_print_stats import calc_print_stats

def main():
    """
    Main function:
    - gets filters by asking for user input
    - loads the data
    - calculates and prints statistics
    """
    
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'} 

    while True:
        
        city, month, weekday = get_filters(CITY_DATA)
    
       
        df = load_data(city, month, weekday, CITY_DATA)
    
        # calculate and print statistics:
        # pass city to take special case of Washington into account
        # pas month, day for special case of all months or all weekdays 
        calc_print_stats (df, city, month, weekday)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    
    start_time = time.time()
    
    main()  
    
    print("\nThis report took %s seconds in total." % (time.time() - start_time))
    print('-'*60)
    
    