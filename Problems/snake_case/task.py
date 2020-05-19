string = input()
output = ""

for letter in string:
    if letter.isupper():
        output += "_"
    output += letter.lower()

print(output)
