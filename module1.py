from decimal import Decimal

def determineIfNumber(x):
    try:
        x = int(x)
        return True
    except Exception as e:
        pass

    try:
        x = Decimal(x)
        return True
    except Exception as e:
        pass

    try:
        x = complex(x)
        return True
    except Exception as e:
        pass

    return False

def sum(x=0, y=0):
    if determineIfNumber(x):
        if determineIfNumber(y):
            if '.' in x or '.' in y:
                return Decimal(x) + Decimal(y)
            else:
                return int(x) + int(y)
        else:
            return "Please enter a number"
    else:
        return "Please enter a number"

def subtract(x=0, y=0):
    if determineIfNumber(x):
        if determineIfNumber(y):
            if '.' in x or '.' in y:
                return Decimal(x) - Decimal(y)
            else:
                return int(x) - int(y)
        else:
            return "Please enter a number"
    else:
        return "Please enter a number"

def multiply(x=0, y=0):
    if determineIfNumber(x):
        if determineIfNumber(y):
            if '.' in x or '.' in y:
                return Decimal(x) * Decimal(y)
            else:
                return int(x) * int(y)
        else:
            return "Please enter a number"
    else:
        return "Please enter a number"

def divide(x=0, y=0):
    if determineIfNumber(x):
        if determineIfNumber(y):
            if '.' in x or '.' in y:
                yDecimal = Decimal(y)
                if yDecimal==0.0:
                    return "Division by zero"
                return Decimal(x) / yDecimal
            else:
                yInt = int(y)
                if yInt == 0:
                    return "Division by zero"
                return int(x) / yInt
        else:
            return "Please enter a number"
    else:
        return "Please enter a number"

if "__main__" == __name__:

    print("Part 1\nPlease enter 2 numbers to be summed and then subtracted")
    x = input("First number: ")
    y = input("Second number: ")

    print(f"Sum: {x} + {y} = {sum(x, y)}")
    print(f"Subtract: {x} - {y} = {subtract(x, y)}")

    print("Part 2\nPlease enter 2 numbers to be multiplied and then divided")
    x = input("First number: ")
    y = input("Second number: ")
    print(f"Multiply: {x} * {y} = {multiply(x, y)}")
    print(f"Divide: {x} / {y} = {divide(x, y)}")



