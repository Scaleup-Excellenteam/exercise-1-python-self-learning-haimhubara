"""
This module provides date-related functions.
Functions:
- is_valid_date(date_str): Checks if the date is in a valid format (YYYY-MM-DD).
- no_vinaigrette(date1, date2): Generates a random date between two given dates and checks if the date is a Wednesday. If it's a Wednesday, it prints "I don't have vinegar".
 Otherwise, it prints "Ain't gettin' no vinaigrette today :(". Returns the random date and the corresponding day of the week.
"""
import datetime
import random


TIME_FORMAT = "%Y-%m-%d"

def is_valid_date(date_str):
    """Check if the date is in a valid format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_str, TIME_FORMAT)
        return True
    except ValueError:
        return False

def no_vinnigrete(date1, date2):
    """Generate a random date between two given dates and check if the date is a Monday.
    If it is, print a message saying "Ain't gettin' no vinaigrette today :(".
    """
    # Check if the date format is valid
    if not is_valid_date(date1) or not is_valid_date(date2):
        print("Invalid date format")
        return None, None

    # The start date is the minimum between the two dates
    start = datetime.datetime.strptime(min(date1, date2), TIME_FORMAT).date()

    # The end date is the maximum between the two dates
    end = datetime.datetime.strptime(max(date1, date2), TIME_FORMAT).date()

    # Generate random days between start date and end date
    random_days = random.randint(0, (end - start).days)

    # The random day is the start day + the days we generate
    random_date_generated = start + datetime.timedelta(days=random_days)

    day_in_week = random_date_generated.weekday()

    if day_in_week == 0:
        print("Ain't gettin' no vinaigrette today :(")

    return random_date_generated.strftime(TIME_FORMAT), day_in_week

if __name__ == "__main__":
    start_date = input("Enter first date (YYYY-MM-DD): ")
    end_date = input("Enter second date (YYYY-MM-DD): ")

    random_date = no_vinnigrete(start_date, end_date)
    if random_date[0]:
        print(f"The random date is {random_date[0]} and the weekday index is {random_date[1]}")
