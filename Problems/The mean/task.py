sum_ = 0
count = 0
while True:
    input_ = input()
    if input_ == ".":
        break
    sum_ += int(input_)
    count += 1

print(sum_ / count)
