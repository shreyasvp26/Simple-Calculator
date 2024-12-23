logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    if(n1>n2):
        return n1-n2
    return n2-n1
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
def Calculator():
    loop = True
    print(logo)
    num1 = float(input("What is the first number ? "))
    while loop :
        print("+ \n- \n* \n/")
        op = input("Pick an operation : ")
        num2 = float(input("What is the second number ? "))
        ans = operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {ans}")
        c = input(f"Type 'y' to continue calculating with {ans}, otherwise to start new calculation type 'n': ")
        if c == 'y':
            num1 = ans
        else:
            loop = False
            print("\n"*50)
            Calculator()

Calculator()