import datetime
import random

def is_valid_date(date_str):
    """ 
    check if the date is valid format (YYYY-MM-DD)

    params: string format (YYYY-MM-DD)
    return: is valid date or not
    """
    

    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def no_vinnigrete(date1, date2):
      """ 
      generate random date between two given dates 
          and check if the date is wednesday if it is we print message no vinniger

      params: to strings format (YYYY-MM-DD) 
      return: random year between date1 and date2 and random day
    """

    # check if the date valid
    if not is_valid_date(date1) or not is_valid_date(date2):
        return "Invalid date format"

    # the format of the date
    time_format = "%Y-%m-%d"

    # the start date is the minimum between the two dates
    start_date = datetime.datetime.strptime(min(date1, date2), time_format).date()

    # the end date is the maximum between the two dates
    end_date = datetime.datetime.strptime(max(date1, date2), time_format).date()

    # generate random days between start date to end date
    random_days = random.randint(0, (end_date - start_date).days)

    #the randon day is the start day + the days we generate
    random_date_generated = start_date + datetime.timedelta(days=random_days)

    day_in_week = random_date_generated.weekday()

    if day_in_week == 2:
        print("I dont have vinegar")

    return random_date_generated.strftime(time_format),day_in_week

if __name__ == "__main__":
    random_date = no_vinnigrete("2020-12-12", "1990-12-12")
    print('the year is', random_date[0] ,'the day in the week is', random_date[1])
