# Control flow

The order in which a programme makes descisions. 
How does it flow from one expression to another. 
It is like following a recipe and how you have to follow the steps in order.
You can do this using loops and if statements. There are no switch statements.

## Conditional statements (if and elif)

An if statement is implemented if something is true and not implemented if it is false. 
Example:

```python
if age > 18:
    print("You can watch all movies")
```

Elif stands for else if. This is if you want to carry on as well as the previous statement.
```python
if age >= 18:
    print("You can watch all movies")
elif age >= 16:
    print("Sorry you cant watch 18 rated movies, but you can watch 15 rated movies")
```
Else is a 'catch all'. There is no condition. So if no if or elif statments are true then the else clause will be used.
```python
else:
    print("You can only watch U rated movies")
```

## Loops 

There are for and while loops.
Loops are iterative and cycle through data. 

### For loop
The layout is for num in variable. It iterates over each number (num). 


Example for loop:
```python
for num in list_data:
    print(num * 2)
```
You can have for loops within for loops for embedded lists:
```python
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
```
And in dictionaries:

```python
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```

### While loops

Monitors a condition to see if it is still the case.
Example: 
```python
x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1
```

