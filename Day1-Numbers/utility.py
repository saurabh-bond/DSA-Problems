

# get multiple numbers from user
# 
def get_multiple_numbers_new_line():
    numbers = []
    print("Multiple numbers on new line. \n ")
    while True:
        user_input = input("Enter a number (or 'done' to stop): ")
        if user_input.lower() == 'done':
            break
        numbers.append(int(user_input))
    return numbers