from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a / b

def calculate():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': subtract
    }

    first_number = float(input("What's the first number?: "))

    while True:
        print('\n'.join(operations.keys()))
        sign = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        operation = operations[sign]
        result = operation(first_number, second_number)

        pick = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if pick == 'y':
            first_number = result
        else:
            first_number = float(input("What's the first number?: "))
            # calculate() - Recursion alternative (not effective)

if __name__ == "__main__":
    print(logo)
    calculate()