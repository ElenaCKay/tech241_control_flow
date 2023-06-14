# Control flow task 4 - While loops

# 4.1 take 10 integers from the user and print their average

# count = 0
#
# for x in range(10):
#     num = int(input("Pick a number  "))
#     count += num
#
# print(count / 10)

# 4.2 Write a while loop to print the following series: 10, 20, 30, 40

# count = 0
#
# while count < 300:
#     count += 10
#     print(count)

# 4.3 Upgrade your waiter program to only allow items from the menu

# menu = {
#     "starters": ["soup", "olives", "chicken strips", "nachos"],
#     "mains": ["pizza", "burger", "sushi", "ramen", "hot dog"],
#     "desserts": ["cheesecake", "ice-cream", "milkshake", "tiramisu"]
# }
#
# guest_list = []
#
# while len(guest_list) == 0:
#     print("Hello, here are the starters:")
#     print(menu["starters"])
#
#     guest_starter = input("What would you like for your starter? ")
#     if guest_starter in menu["starters"]:
#         guest_list.append(guest_starter)
#     else:
#         print("That is not on the menu!")
#
#
#     while len(guest_list) == 1:
#         print("Here are the mains:")
#         print(menu["mains"])
#
#         guest_main = input("What would you like for your main? ")
#         if guest_main in menu["mains"]:
#             guest_list.append(guest_main)
#         else:
#             print("That is not on the menu!")
#
#         while len(guest_list) == 2:
#             print("Here are the deserts:")
#             print(menu["desserts"])
#
#             guest_dessert = input("What would you like for dessert? ")
#             if guest_dessert in menu["desserts"]:
#                 guest_list.append(guest_dessert)
#             else:
#                 print("That is not on the menu!")
#
#
# print(f"You have ordered the {guest_list[0]}, the {guest_list[1]} and the {guest_list[2]}.")

# 4.4 Take all the numbers until the user enter 0 then sum all the positive and all the negative and print them back

positive_num = 0
negative_num = 0

user_input = int(input("Type in a number "))

if user_input > 0:
    positive_num += user_input
else:
    negative_num += user_input

while user_input != 0:
    user_input = int(input("Type in a number "))
    if user_input > 0:
        positive_num += user_input
    else:
        negative_num += user_input

print(f"The positive numbers summed up to {positive_num} and the negative numbers summed up to {negative_num}")
