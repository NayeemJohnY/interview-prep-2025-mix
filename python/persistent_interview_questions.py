# Problem 1
li = ["SBI$22$", "HDFC$8$", "KOTAK$122$", "ICICI$31$", "RBI$50$"]

# Solution 1
out = sorted(li, key=lambda x: int(x.split('$')[1]))
print(out)


# Problem 2
# Solution 1
input = "All that glitters is not gold"
words = input.split(" ")
print(words)
reverse_string= ""
for word in words:
    rev = ""
    for i in range(len(word)-1, -1, -1):
        rev += word[i]
    reverse_string += rev + " "

print(reverse_string.strip())

# Solution 2
print(" ".join(word[::-1] for word in input.split()))




