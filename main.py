import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,

    }
def calculator():
    print(art.logo)
    should_accumulate = True
    no1=float(input("What's the first number?"))

    while should_accumulate:
        for symbols in operations:
            print(symbols
        )
        choice_operations=(input("Pick an operation"))
        no2=float(input("What's the next number?"))

        if choice_operations in operations:
            calculation=operations[choice_operations]
            result=calculation(no1, no2)
            print(f"{no1} {choice_operations} {no2} = {result}")

        else:
            print(f"This is invalid! Please choose +, - , *, / only.")

        restart=input(f"Type 'y' if you want to continue calculating with {result},or type 'n' to start a new calculation.\n").lower()

        if restart == "y":
            no1=result

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()