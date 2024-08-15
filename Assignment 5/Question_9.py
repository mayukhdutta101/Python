# Print the season name of the year based on the month number using a dictionary.

season_dict = {
    1: 'Winter',  # January
    2: 'Winter',  # February
    3: 'Spring',  # March
    4: 'Spring',  # April
    5: 'Spring',  # May
    6: 'Summer',  # June
    7: 'Summer',  # July
    8: 'Summer',  # August
    9: 'Autumn',  # September
    10: 'Autumn', # October
    11: 'Autumn', # November
    12: 'Winter'  # December
}

month_number = int(input("Enter the month number: ")) 
season = season_dict.get(month_number, 'Invalid month number')
print(f"The season for month {month_number} is {season}.")
