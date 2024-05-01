print("this is odoh joshua smith calculator")

def generate_calculator_art():
    calculator_art = """
                     _____________________
                    |  _________________  |
                    | |  7  |  8  |  9  | |
                    | |_____|_____|_____| |
                    | |  4  |  5  |  6  | |
                    | |_____|_____|_____| |
                    | |  1  |  2  |  3  | |
                    | |_____|_____|_____| |
                    | |  0  |  .  |  =  | |
                    | |_____|_____|_____| |
                    |_____________________|
    """
    print(calculator_art)

generate_calculator_art()







def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

The_operator = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(float(input("Enter a number: ")))

for symbol in The_operator:
    print(symbol)
def calculation():
    should_continue = True
    while should_continue:
        pick_out_operator = input("Choose any operator you want to use: ")
        num2 = int(float(input("Enter a number: ")))

        result = The_operator.get(pick_out_operator)
        if result:
            answer = result(num1, num2)
            print(answer)
            num3 = int(float(input("Enter a number: ")))
            pick_out_operator = input("Enter the operator: ")
            result = The_operator.get(pick_out_operator)
            if result:
                answer_ = result(answer, num3)
                print(answer_)
                if input("Do you want to continue? Type 'Yes' to continue or 'No' to exit: ") != "Yes":
                    should_continue = False
            else:
                print("Invalid operator!")
        else:
            print("Invalid operator!")
            calculation()
calculation()
