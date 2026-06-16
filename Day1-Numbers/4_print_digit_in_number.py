

def print_digit_in_number(num):
    while num > 0:
        digit = int(num % 10)
        print(f"Digits are: {digit}")
        num = int(num / 10)

print(f"Digits in 1001 are: \n")
print_digit_in_number(1001)
