##What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
##
##You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
##
##Input: Year as an int.
##
##Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
##
##Example:
##
##most_frequent_days(2427) == ['Friday']
##most_frequent_days(2185) == ['Saturday']
##most_frequent_days(2860) == ['Thursday', 'Friday']
##
##Preconditions: Year is between 1 and 9999. Week starts with Monday.

import datetime

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def most_frequent_days(year):
    days_dict = dict()
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year+1, 1, 1)
    for single_date in daterange(start_date, end_date):
        if single_date.weekday() in days_dict.keys():
            days_dict[single_date.weekday()] += 1
        else:
            days_dict[single_date.weekday()] = 1
    day_max = max(days_dict.values())        
    return [days[key] for key,val in days_dict.items() if val == day_max] 

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"

