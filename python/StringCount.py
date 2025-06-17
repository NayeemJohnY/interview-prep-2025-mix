s = "Automat@123ionssss&"
specialchars, numbers, letters = 0, 0, 0
for i in range(len(s)):
    if s[i].isalpha():
        letters += 1
    elif s[i].isdigit():
        numbers += 1
    else:
        specialchars += 1
print('Letters Count', letters)
print('Numbers Count', numbers)
print('SpecialChars Count', specialchars)
