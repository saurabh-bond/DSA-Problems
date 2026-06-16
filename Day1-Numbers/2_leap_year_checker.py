
""" 
2 conditions for a leap year
----------
1. Divisible by 4 and should not be divisible by 100
2. Exception: if divisible by 400, then okay.
"""
def is_leap_year(year: int) -> str:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Year {year} is a leap year.")
    else:
        print(f"Year {year} is not a leap year.")



# Tests
from utility import get_multiple_numbers_new_line

entered_years = get_multiple_numbers_new_line()
for year in entered_years:
    is_leap_year(year)
