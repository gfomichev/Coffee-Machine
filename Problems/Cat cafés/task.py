max_ = input().split()
while True:
    cafe = input().split()
    if cafe[0] == "MEOW":
        print(max_[0])
        break
    if int(cafe[1]) > int(max_[1]):
        max_ = cafe
