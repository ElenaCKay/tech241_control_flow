# Control flow
# Giving python an order in which to do things

# Conditional statements

# Check an age and see if the person can watch a film
user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) < 120:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 120")

number_age = int(age)

if number_age >= 18:
    print("You can watch all movies")
elif number_age >= 16:
    print("Sorry you cant watch 18 rated movies, but you can watch 15 rated movies")
elif number_age >= 13:
    print("Sorry you cant watch 18 or 15 rated movies, but you can watch 15 rated movies")
elif number_age >= 9:
    print("Sorry you cant watch 18, 15 or 12 rated movies, but you can watch all other movies")
else:
    print("You can only watch U rated movies")

