income = int(input())
percent = 28 if income >= 132407 else 25 if income >= 42708 else 15 if income >= 15528 else 0
calculated_tax = round(income * percent / 100)
string = f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!"
print(string)
