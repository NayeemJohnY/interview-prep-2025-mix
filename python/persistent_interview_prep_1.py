
# Problem 1: List & Array — Find Duplicate Elements
input = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# Solution 1
visited = []
duplicate = set()
for item in input:
    if item in visited:
        duplicate.add(item)
    else:
        visited.append(item)
print(duplicate)


# Problem 2: Set & Tuple — Intersection of Unique Pairs
list1 = [(1,2), (3,4), (5,6), (1,2)]
list2 = [(3,4), (7,8), (1,2), (9,10)]

# Output:
# {(1,2), (3,4)}
intersection = {item for item in list1 if item in list2}
print(intersection)


# Problem 3: Dictionary — Frequency Count and Sort
# Input: "testing"
# Output: {'t': 2, 'e': 1, 's': 1, 'i': 1, 'n': 1, 'g': 1}

# Solution 1
from collections import Counter
input = "testing"
count_map = Counter(input)
print("Map: ", count_map)
count_map = dict(sorted(count_map.items(), key=lambda item : item[1], reverse=True))
print(count_map)

#  Solution 2
freq_map = {}
for ch in input:
    freq_map[ch] = freq_map.get(ch, 0) + 1
    # if ch in freq_map:
    #     freq_map[ch] = freq_map[ch] + 1
    # else:
    #     freq_map[ch] = 1
freq_map = dict(sorted(freq_map.items(), key=lambda item : item[1], reverse=True))
print(freq_map)

  
# Problem 4: String & List — Check Anagram
# Input: "listen", "silent"
# Output: True

# Input: "hello", "world"
# Output: False
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    # # Solution 1
    # l1 = sorted(str1)
    # l2 = sorted(str2)
    # return  l1 == l2

    # Solution 2
    freq_map = {}
    for ch in str1:
        freq_map[ch] = freq_map.get(ch, 0) + 1
        # freq_map[ch] = freq_map[ch] + 1 if ch in freq_map else 1
    for ch in str2:
        if ch not in freq_map:
            return False
        # freq_map[ch] = freq_map[ch] - 1 if ch in freq_map else 1
        freq_map[ch] -= 1
        if freq_map[ch] == 0:
            del freq_map[ch]
    
    return not freq_map
        

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

# Problem 5: List & Dictionary — Group Words by Length
# Output: {3: ['cat', 'dog', 'ant'], 4: ['bird', 'lion'], 8: ['elephant']}
input= ["cat", "dog", "bird", "lion", "ant", "elephant"]
# Solution 1
word_count_map = {}
for word in input:
    length = len(word)
    word_count_map[length] = word_count_map.get(length, []) + [word]
    # if length in word_count_map:
    #     word_count_map[length].append(word)
    # else:
    #     word_count_map[length] = [word]
print("word_count_map: ", word_count_map)

# Solution 2
from collections import defaultdict
grouped = defaultdict(list)
for word in input:
  grouped[len(word)].append(word)
print(dict(grouped))

