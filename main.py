def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    pass

def remainder(a, b):
    pass

def sqrt(a):
    pass

def pow(a, b):
    return a ** b # raise a to the power of b

if __name__ == '__main__':
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print("These are your numbers", num1, num2)

    print("Multiply:", multiply(a, b))
    print("Pow:", pow(a, b))
    # print("Square Root:", sqrt(a, b))