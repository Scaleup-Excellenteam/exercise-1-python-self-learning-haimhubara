"""
This module provides date-related functions.
Functions:
- is_valid_date(date_str): Checks if the date is in a valid format (YYYY-MM-DD).
- no_vinaigrette(date1, date2): Generates a random date between two given dates and checks if the date is a Wednesday. If it's a Wednesday, it prints "I don't have vinegar". Otherwise, it prints "Ain't gettin' no vinaigrette today :(". Returns the random date and the corresponding day of the week.
"""

import datetime
import random

def is_valid_date(date_str):
    """Check if the date is in a valid format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def no_vinaigrette(date1, date2):
    """Generate a random date between two given dates and check if the date is a Wednesday.
    If it is, print a message saying "I don't have vinegar."
    """
    # Check if the date format is valid
    if not is_valid_date(date1) or not is_valid_date(date2):
        return "Invalid date format"

    # The format of the date
    time_format = "%Y-%m-%d"

    # The start date is the minimum between the two dates
    start_date = datetime.datetime.strptime(min(date1, date2), time_format).date()

    # The end date is the maximum between the two dates
    end_date = datetime.datetime.strptime(max(date1, date2), time_format).date()

    # Generate random days between start date and end date
    random_days = random.randint(0, (end_date - start_date).days)

    # The random day is the start day + the days we generate
    random_date_generated = start_date + datetime.timedelta(days=random_days)

    day_in_week = random_date_generated.weekday()

    if day_in_week == 2:  # Wednesday
        print("I don't have vinegar")
    else:
        print("Ain't gettin' no vinaigrette today :(")

    return random_date_generated.strftime(time_format), day_in_week


if __name__ == "__main__":
    random_date = no_vinaigrette("2020-12-12", "1990-12-12")
    print('The random date is', random_date[0], 'and the day of the week is', random_date[1])
