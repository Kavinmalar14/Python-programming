def add(a,b):
    print(a + b)

def subtract(a,b):
    print(a - b)

def multiply(a,b):
    print(a * b)

def divide(a,b):
        print(a/b)

print("Calculator")
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
calculation = input("What calculation woud you like to do? ")

if calculation == add:
    try:
        result = (a + b)
    except ValueError:
        print(a + b)

elif calculation == subtract:
    try:
        result = (a - b)
    except ValueError:
        print(a - b)

elif calculation == multiply:
    try:
        result = (a * b)
    except ValueError:
        print(a * b)

elif calculation == divide:
    try:
        result = (a/b)
    except ValueError:
        print(a/b)

else:
    print("Try again")