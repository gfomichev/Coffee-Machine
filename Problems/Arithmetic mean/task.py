numbers = [int(x) for x in input().split()]
sum_of_numbers = 0
count = 0

for num in numbers:
    sum_of_numbers += num
    count += 1

mean = sum_of_numbers / count
print(mean)
