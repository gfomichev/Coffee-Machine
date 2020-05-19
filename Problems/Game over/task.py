scores = input().split()
# put your python code here
correct = 0
incorrect_count = 0
for score in scores:
    if score == "C":
        correct += 1
    elif incorrect_count < 2:
        incorrect_count += 1
    else:
        print("Game over")
        break
else:
    print("You won")
print(correct)
