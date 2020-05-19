# put your python code here
sum_ = 0
squared_sum = 0
while True:
    num = int(input())
    sum_ += num
    squared_sum += num ** 2
    if sum_ == 0:
        print(squared_sum)
        break
