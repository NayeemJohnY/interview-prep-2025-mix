
# https://leetcode.com/problems/valid-palindrome/description/
# 125. Valid Palindrome
from typing import List
import re
print("125. Valid Palindrome")


def isPalindrome(s: str) -> bool:
    rev = re.sub("[^0-9a-z]", "", s.lower())
    return rev == "".join(rev[::-1])


assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True

# https://leetcode.com/problems/reverse-words-in-a-string
print("151. Reverse Words in a String")


def reverseWords(s: str) -> str:
    return " ".join(word for word in s.strip().split(" ")[::-1] if word.strip() != "")


assert reverseWords("the sky is blue") == "blue is sky the"
assert reverseWords("  hello world  ") == "world hello"
assert reverseWords("a good   example") == "example good a"

# https://leetcode.com/problems/longest-palindromic-substring/
print("5. Longest Palindromic Substring")


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


def longestPalindrome(s: str) -> str:
    longest_substring = ""
    for i in range(len(s)):
        s1 = expandAroundCenter(s, i, i)
        s2 = expandAroundCenter(s, i, i+1)
        substring = s1 if len(s1) > len(s2) else s2
        if (len(substring) > len(longest_substring)):
            longest_substring = substring
    return longest_substring


assert longestPalindrome("babad") == "bab"
assert longestPalindrome("cbbd") == "bb"


# https://leetcode.com/problems/reverse-string
print("344. Reverse String")


def reverseString(s: List[str]) -> None:
    # Solution 1
    left = 0
    right = len(s)-1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
assert s == ["o", "l", "l", "e", "h"]
s = ["H", "a", "n", "n", "a", "h"]
reverseString(s)
assert s == ["h", "a", "n", "n", "a", "H"]

# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence
print("2042. Check if Numbers Are Ascending in a Sentence")


def areNumbersAscending(s: str) -> bool:
    nums = [int(num_str)
            for num_str in re.sub("[^0-9]+", " ", s).strip().split()]
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            return False
    return True


assert areNumbersAscending(
    "1 box has 3 blue 4 red 6 green and 12 yellow marbles") == True
assert areNumbersAscending("hello world 5 x 5") == False
assert areNumbersAscending(
    "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s") == False


# https://leetcode.com/problems/string-to-integer-atoi/
print("8. String to Integer (atoi)")


def myAtoi(s: str) -> int:
    signed = None
    num_str = ""
    for c in s:
        if not num_str and signed is None:
            if c == " ":
                continue
            if c == "-":
                signed = True
                continue
            if c == "+":
                signed = False
                continue
        if not c.isdigit():
            break
        num_str += c
    num = int(num_str) if num_str else 0
    num = num * (-1 if signed == True else 1)
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    if num > INT_MAX:
        num = INT_MAX
    elif num < INT_MIN:
        num = INT_MIN
    return num


assert myAtoi("42") == 42
assert myAtoi("   -042") == -42
assert myAtoi("1337c0d3") == 1337
assert myAtoi("0-1") == 0
assert myAtoi("words and 987") == 0
assert myAtoi("-91283472332") == -2147483648
assert myAtoi("+1") == 1
assert myAtoi("+-12") == 0
assert myAtoi("   +0 123") == 0
assert myAtoi("  +  413") == 0

# https://leetcode.com/problems/count-and-say/
print("38. Count and Say")


def get_rle(s):
    rle = ""
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            rle += f"{counter}{s[i-1]}"
            counter = 1
    rle += f"{counter}{s[len(s)-1]}"
    return rle


def countAndSay(n: int) -> str:
    if n == 0:
        return ""

    s = "1"

    for _ in range(1, n):
        s = get_rle(s)
    return s

assert countAndSay(1) == "1"
assert countAndSay(4) == "1211"
assert countAndSay(5) == "111221"

# https://leetcode.com/problems/valid-anagram
print("242. Valid Anagram")
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    map = {}
    for c in s:
        map[c] = map.get(c, 0) + 1
    for c in t:
        if c not in map:
            return False
        map[c] -=1
        if map[c] == 0:
            del map[c]
    return not map


assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False


# https://leetcode.com/problems/first-unique-character-in-a-string
print("387. First Unique Character in a String")
def firstUniqChar(s: str) -> int:
    map = {}
    for c in s:
        map[c] = map.get(c, 0)+1
    for i in range(0, len(s)):
        if map[s[i]] == 1:
            return i
    return -1

assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1  


# https://leetcode.com/problems/group-anagrams
print("49. Group Anagrams")
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    map = {}
    for word in strs:
        key = tuple(sorted(word))
        map[key] = map.get(key, []) + [word]
    return list(map.values())

assert groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
print("3. Longest Substring Without Repeating Characters")
def lengthOfLongestSubstring(s: str) -> int:
    left, right, maxLen = 0, 0, 0
    chars_set = set()
    while right < len(s):
        if s[right] not in chars_set:
            chars_set.add(s[right])
            maxLen = max(maxLen, right-left+1)
            right += 1
        else:
            chars_set.remove(s[left])
            left += 1
    return maxLen

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3

def minWindow(s: str, t: str) -> str:
    left, right = 0, 0
    while right < len(s):
        for c in t:
            if c != s[right]:
                break
        right += 1
    print(right)

minWindow("ADOBECODEBANC", "ABC")