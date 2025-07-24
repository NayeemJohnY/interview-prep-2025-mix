# Screening


import requests
from typing import List
# Return True if target sum from the items else False


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map:
            return True
    return False

# L1
# Return the longest substring without repeating characters


# Input: "abcabcbb"
# Output: "abc"
# input = "abcabcbb"
input = "aabbcdefg"
left, right = 0, 0
maxLen = 0
chars_set = set()
best_start = 0
while right < len(input):
    if input[right] not in chars_set:
        chars_set.add(input[right])
        if right - left + 1 > maxLen:
            maxLen = right - left + 1
            best_start = left
        right += 1
    else:
        chars_set.remove(input[left])
        left += 1
print(input[best_start:best_start+maxLen])


class APIBase():

    def __init__(self, host_url, *args, **kwargs):
        self.host_url = host_url

    def get(self, path=None, query: dict = None):
        url = self.host_url + "/" + path
        for k, v in query.items():
            url += f"?{k}={v}"
            url += "&"
        print("Requesting get Call on URL", url)
        response = requests.get(url=url)
        assert response.status_code == 200, f"response code is {response.status_code}"
        return response.json()

    def get_data(self, data, key):
        for d in data:
            if d["first_name"] == key:
                return d["avatar"]
        return "Not Found"


api_base = APIBase("https://reqres.in/api")
avatar = api_base.get_data(api_base.get(
    path="users", query={"page": 2})["data"], "Michael")
print(avatar)

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true
#  1 2 2 2 1

# Input: head = [1,2]
# Output: false

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next:ListNode = None
    
    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}" 
        
def is_palindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    fast = head
    print("fast", fast)
    prev = reverse(slow)
    print("fast1", fast)
    print(prev)
    slow = slow.next
    while (slow):
        if slow.val != fast.val:
            return False
        slow = slow.next
        fast = fast.next
    return True

# 1 2 3 2 1
#  3.next = 2.next
#  2.next = 1.next
# 1 3 3 1 2
def reverse(node):
    prev = None
    current = node
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
    

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(2)
a.next.next.next.next.next = ListNode(1)

print(is_palindrome(a))


def is_palindrome_number(x):
    if x < 0:
        return False
 # 121 % 10 = > 1 , 121 // 10 = 12
# 12 % 10 => 2
    rev = 0
    temp = x
    while temp > 0:
      rem = temp % 10
      rev = rev * 10 + rem
      temp = temp // 10
    return x == rev

for i in [121, -121, 1221, 22422, 77899, 8888]:
    print(i, is_palindrome_number(i))
