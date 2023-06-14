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

for num in list_data:
    if num == 3:
        print("You have found 3!")
    elif num > 3:
        print("Gone too far")
    else:
        print("Too soon!")