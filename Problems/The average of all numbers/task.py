# put your python code here
a = int(input())
b = int(input())
count = 0
sum_ = 0

for num in range(a, b + 1):
    if num % 3 == 0:
        count += 1
        sum_ += num

print(sum_ / count)
