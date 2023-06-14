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



