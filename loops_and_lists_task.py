# Control flow task 3

# Make a loop that says hello 10 times

# for x in range(10):
#     print("Hello")

# Create a loop with a range that asks for names and appends to a list called list_names

# list_names = []
#
# for x in range(5):
#     list_names.append(input("List a name "))
#
# print(list_names)
#
# # Make a loop that iterates over each name in list_name and formats it into lowercase
#
# list_names_lower = []
#
# for name in list_names:
#     list_names_lower.append(name.lower())
#
# print(list_names_lower)
#
# # Iterate over a list of numbers and print the even ones
#
# number_list = [1, 14, 200, 3, 6, 17, 83]
#
# for number in number_list:
#     if number % 2 == 0:
#         print(number)

# Iterate over all number from 0 to 100 and add them together

count = 0

for x in range(100):
    count += x

print(count)

# Add all the odd numbers together

count = 0

for x in range(100):
    if x % 2 != 0:
        count += x
print(count)

# Add all the even numbers together

count = 0

for x in range(100):
    if x % 2 == 0:
        count += x
print(count)