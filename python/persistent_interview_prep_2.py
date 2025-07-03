# 🔧 Problem 1: Log File Parsing
# Scenario: You are testing a backend service. You receive a multiline string representing server logs. Extract all ERROR messages with timestamps.

# Input (multiline string):
import string
import itertools
logs = """2025-07-02 10:00:01 INFO Service started
2025-07-02 10:01:22 ERROR Failed to connect to DB
2025-07-02 10:02:45 DEBUG Heartbeat
2025-07-02 10:03:10 ERROR Null pointer exception
"""
error_logs = [log for log in logs.split("\n") if "ERROR" in log]
print(error_logs)

# 🧪 Problem 2: JSON Response Validator
# Scenario: You call an API and get a JSON response. Validate that all fields in a required schema exist and none are empty.
response = {
    "user": {"id": 123, "name": "Alice", "email": "alice@example.com"},
    "status": "active"
}
required_fields = ["user.id", "user.name", "user.email", "status"]

def key_in_dict(d, path):
    for key in path.split("."):
        if key not in d:
            return False
        d = d[key]
    return True

def validate_response(response: dict, required_fields):
    for field in required_fields:
        if not key_in_dict(response, field):
            return False
    return True


print(validate_response(response, required_fields))
required_fields.append("company")
print(validate_response(response, required_fields))
# 📊 Problem 3: CSV Test Data Filter
# Scenario: You are testing a form upload feature. A CSV contains user info. You need to extract rows where age > 25 and country is India.


# Input (list of dicts):
# output : [{"name": "Priya", "age": 28, "country": "India"}]
csv_data = [
    {"name": "Raj", "age": 24, "country": "India"},
    {"name": "John", "age": 30, "country": "USA"},
    {"name": "Priya", "age": 28, "country": "India"},
]
filtered_data = []
for data in csv_data:
    if data['age'] > 25 and data['country'] == "India":
        filtered_data.append(data)
print(filtered_data)

# ⚙️ Problem 4: Test Case Generator (Strings)
# Scenario: Create all possible test cases for a form that accepts a username of length 3, containing only lowercase letters.

# Output (sample):
# ['aaa', 'aab', ..., 'zzz']
res = [''.join(p) for p in itertools.product(
    string.ascii_lowercase, repeat=3)]
print(len(res))


# ✅ Problem 5: HTML Tag Validator
# Scenario: As part of a UI test, you’re given a string that might contain HTML-like tags. Write a function to validate whether all tags are properly opened and closed.

# Input:

import re
def is_valid_html(html):
    tags = re.findall("<(/?)(\w+)>", html)
    stack = []
    for tag in tags:
        if "/" == tag[0]:
            if not stack or stack.pop()[1] != tag[1]:
                return False
        else:
            stack.append(tag)
    return not stack
            
print(is_valid_html("<div><p>Test</p></div>"))
print(is_valid_html("<div><p>Test</div></p>"))