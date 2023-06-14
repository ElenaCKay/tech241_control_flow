# Loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

# for num in list_data:
#     print(num * 2)

# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# Looping through dictionaries

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)

# Loop that returns money

# for items in dict_data.values():
#     print(items["money"])

# Loops and if statements

# for num in list_data:
#     if num == 3:
#         print("You have found 3!")
#     elif num > 3:
#         print("Gone too far")
#     else:
#         print("Too soon!")

# While loops

#x = 0

# while x < 10:
#     print(f"it's working -> {x}")
#     x += 1

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# Verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 120:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 120")

print(f"Your age is {age}")