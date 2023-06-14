# Task 2.1 -> Odd or even number

# user_number = int(input("Please type in a digit... "))
#
# if user_number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Task 2.2 -> FizzBuzz

count = 0

while count < 100:
    count += 1
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)