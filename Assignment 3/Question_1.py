# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    month = month.lower()
    if month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    elif month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    else:
        return "Invalid month"
    
month = input("Enter the name of the month: ")
season = check_season(month)
print(f"The {month.capitalize()} month falls under {season} season.")