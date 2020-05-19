# put your python code here
first = float(input())
second = float(input())
operation = input()
if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "/":
    print(first / second if second != 0 else "Division by 0!")
elif operation == "*":
    print(first * second)
elif operation == "mod":
    print(first % second if second != 0 else "Division by 0!")
elif operation == "pow":
    print(first ** second)
elif operation == "div":
    print(first // second if second != 0 else "Division by 0!")
