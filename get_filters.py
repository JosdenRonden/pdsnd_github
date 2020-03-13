
# If one has a typo on the prompt for the city, suggest a city by identifying
# the closest match. 
# For assessing the similarity between strings, we can use SequenceMatcher; see:
# https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-string

from difflib import SequenceMatcher

def find_match (item, lst_items):
    similarity = 0
    for i, lst_item in zip (range (len(lst_items)), lst_items):
        if (SequenceMatcher(None, item, lst_item).ratio() > similarity):
            similarity = SequenceMatcher(None, item, lst_item).ratio() 
            idx = i
    return idx

def get_filters(city_data):
    """
    Asks user to specify a city, month, and day to analyze.
    - user can input city Chicago, New York City, or Washington; if typo, closest match is suggested
    - user can input month with its first three letters or full 
      (actually, if first three characters are correct, it will continue) 
    - user can inputday of the week with its first three letters or full
    
    Returns:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or all months
        (str) day   - name of the day of week to filter by, or all weekdays
    """

    print("Hello! Let's explore some US bikeshare data!")
    print("****** Data available for Chicago, New York City, and Washington. ******\n")

    # create a list with city names from the keys, with the city name in title case (needed
    # to check whether the inputted city is in the list of cities)
    # https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
    # https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
    cities = [x.title() for x in list(city_data.keys())]
    
    # Ask for city --- spelling errors allowed, or something like nyc :-)
    while True:
        inp_city = input("City to display the results for (press ENTER for Chicago): ").title ()
        if inp_city == "":
            city = "Chicago"
            break
        elif inp_city in cities:
            city = inp_city
            break
        else: #maybe a typo or an abbreviation given as input; suggest closest match 
            idx_city = find_match (inp_city, cities)
            get_answer = str(input("Did you mean {} (Y/N)".format (cities[idx_city]))) 
            if get_answer.upper () == "Y": 
                city = cities[idx_city]
                break
                
    # Ask for month
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "All"]
    while True:
        month = input("Month to display the results for (Jan ... Jun; press ENTER key or type All for all months): ").title() [0:3]

        # Check if the inputted month is in the list of months or blank
        # We can check with an or operator, or check against a union of lists
        ### union of 2 lists: https://www.geeksforgeeks.org/python-union-two-lists        
        if month =="":
            month = "All"
        if month not in months + ["All"]:
            print ("Please enter first 3 letters of the month\n")
        else:
            break
    
    # Ask for day of the week; same approach as with month    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']        
    while True:
        weekday = input("Weekday to display the results for (Mon ... Sun; press ENTER key or ttpe All for all days): ").title()[0:3]
        if weekday == "":
            weekday = "All"
        if weekday not in weekdays + ["All"]:
            print ("Please enter first 3 letters of the day of the week\n")
        else:
            break

    return city, month,  weekday



