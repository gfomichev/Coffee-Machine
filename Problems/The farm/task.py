Chicken = 23
Goat = 678
Pig = 1296
Cow = 3848
Sheep = 6769

money = int(input())
if money >= Sheep:
    count = money // Sheep
    print(count, "sheep")
elif money >= Cow:
    count = money // Cow
    print(count, "cows" if count > 1 else "cow")
elif money >= Pig:
    count = money // Pig
    print(count, "pigs" if count > 1 else "pig")
elif money >= Goat:
    count = money // Goat
    print(count, "goats" if count > 1 else "goat")
elif money >= Chicken:
    count = money // Chicken
    print(count, "chickens" if count > 1 else "chicken")
else:
    print("None")
