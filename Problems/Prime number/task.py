num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("This number is not prime")
        break
else:
    if num == 1:
        print("This number is not prime")
    else:
        print("This number is prime")
