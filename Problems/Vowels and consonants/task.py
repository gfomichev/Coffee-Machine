string = input()
vowel = 'aeiou'
for char in string:
    if char.isalpha() is not True:
        break
    if char in vowel:
        print("vowel")
    else:
        print("consonant")
