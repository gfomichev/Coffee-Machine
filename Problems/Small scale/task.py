min_ = float(input())
while True:
    number = input()
    if number == ".":
        break
    number = float(number)
    if number < min_:
        min_ = number

print(min_)
