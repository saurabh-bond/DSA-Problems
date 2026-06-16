def print_even_or_odd(number):
    if number % 2 == 0:
        print(f"Number {number} is even.")
    else:
        print(f"Number {number} is odd.")



# Tests (Testcases)
from utility import get_multiple_numbers_new_line

# get multiple numbers from user
entered_numbers = get_multiple_numbers_new_line()
for num in entered_numbers:
    print_even_or_odd(num)