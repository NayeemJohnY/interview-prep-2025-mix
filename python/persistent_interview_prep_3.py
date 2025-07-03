# Problem 1: Log File Parser and Analyzer (String, List, Dictionary)
# Scenario: You are given a raw log file content as a single string. Each line in the log represents an event. Some lines contain error messages that start with "ERROR:" and have a timestamp and an error code.

# Input:
# A multi-line string representing log file content.
import re
log_content = """
INFO: User logged in. Timestamp: 2023-01-01 10:00:00
DEBUG: Processing data...
ERROR: [2023-01-01 10:05:15] Code: 500 - Database connection failed.
INFO: Data processed successfully.
ERROR: [2023-01-01 10:10:30] Code: 404 - Resource not found.
WARN: Disk space low.
ERROR: [2023-01-01 10:15:00] Code: 500 - Another database issue.
"""
# Task:
# Parse Error Entries: Extract all error entries. For each error entry, extract the timestamp and error_code.
# Count Error Occurrences: Count the occurrences of each unique error_code.
# Filter by Time: Given a start and end timestamp, return a list of all error messages (full line) that occurred within that time range (inclusive).
error_entries = []
error_count = {}
for log in log_content.splitlines():
    if log.startswith("ERROR"):
        match = re.search(r"\[(.*?)\].*?Code:\s*(\d+)\s*-(.+)$", log)
        if match:
            timestamp_str = match.group(1)
            error_code = match.group(2)
            message = match.group(3)

            # Add to list of error entrieserror_entries
            error_entries.append({
                "timestamp": timestamp_str,
                "error_code": error_code,
                "message": message
            })
            error_count[error_code] = error_count.get(error_code, 0)+1
print(error_entries)
print(error_count)
from datetime import datetime
start_dt = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
end_dt = datetime.strptime("2023-01-01 10:12:00", "%Y-%m-%d %H:%M:%S")
filtered = [
    entry["message"]
    for entry in error_entries
    if start_dt <= datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S") <= end_dt
]
print("filtered", filtered)
print("*" * 130)
### Problem 2: Inventory Management System (Dictionary, List, Tuple, Set)

# **Scenario:** You are building a simplified inventory management system. You need to store product information and manage stock.

# **Input:**

#   * A list of product tuples: `(product_id, product_name, price)`
#   * A dictionary representing current stock: `{'product_id': quantity}`
#   * A list of order requests: `(order_id, product_id, quantity_requested)`
product_data = [
    (101, 'Laptop', 1200.00),
    (102, 'Mouse', 25.00),
    (103, 'Keyboard', 75.00)
]
initial_stock = {
    101: 5,
    102: 10,
    103: 3
}
order_requests = [
    (1, 101, 2),  # Success
    (2, 102, 15), # Fail: Not enough stock
    (3, 104, 1),  # Fail: Product not found
    (4, 103, 1)   # Success
]

# 1.  **Initialize Products:** Given a list of product tuples, create a dictionary
# `products` where keys are `product_id` and values are dictionaries containing `product_name` and `price`.
products = {}
for product in product_data:
    products[product[0]] = {'name': product[1], 'price': product[2]}
print(products)

# 2.  **Process Orders:** For each order request:
#       * Check if the `product_id` exists.
#       * Check if there's enough `quantity` in stock.
#       * If both are true, update the stock and record the successful order.
#       * If not, record it as a failed order with a reason.
successful_orders = []
failed_orders = []
for order in order_requests:
    order_dict = {'order_id' :  order[0], 'product_id':  order[1]}
    try:
        order_dict['quantity'] = order[2]
        if initial_stock[order[1]] >= order[2]:
            successful_orders.append(order_dict)
            initial_stock[order[1]] -= order[2]
        else:
            order_dict['reason'] = 'Not enough stock'
            failed_orders.append(order_dict)
    except KeyError as e:
       order_dict['reason'] = 'Product not found'
       failed_orders.append(order_dict)

print("successful_orders", successful_orders)
print("failed_orders", failed_orders)
print("Final stock", initial_stock)

#  **Generate Low Stock Alert:** Return a set of `product_id`s that have `quantity` below a given threshold.
low_stock_threshold = 2
low_stock = {key for key, value in initial_stock.items() if value <= low_stock_threshold}
print("Low Stock", low_stock)
print("*" * 130)
        
    

# ### Problem 3: Data Deduplication and Aggregation (Set, List, Dictionary)

# **Scenario:** You receive data from multiple sources, and there might be duplicates or slightly varied entries. You need to clean and aggregate this data.

# **Input:**
# A list of strings, where each string represents a data record. Records might be duplicated or contain variations.
# Example:

data_records = [
    "user_id:123, event:login, timestamp:1678886400",
    "user_id:456, event:logout, timestamp:1678886500",
    "user_id:123, event:login, timestamp:1678886400", # Duplicate
    "user_id:789, event:purchase, timestamp:1678886600, item:book",
    "user_id:456, event:logout, timestamp:1678886500", # Another duplicate
    "USER_ID:123, EVENT:LOGIN, TIMESTAMP:1678886400", # Case variation
    "user_id:789, event:purchase, timestamp:1678886700, item:pen"
]

# 1.  **Deduplicate Records:** Remove exact duplicate records, considering case-insensitivity for common fields
# (like `user_id`, `event`). Treat variations in `timestamp` as different records.
unique_records = {record.lower() for record in data_records}
print("unique records", unique_records)

# 2.  **Extract Key-Value Pairs:** For each unique record, parse it into a dictionary of key-value pairs.
parsed_records = []
for record in unique_records:
    records_dict = {}
    for entry in record.split(","):
        key, value = entry.split(":", 1)
        records_dict[key.strip()] = value.strip()
    parsed_records.append(records_dict)
print("parsed records", parsed_records)

# 3.  **Aggregate Event Counts:** Count the total occurrences of each unique `event` across all unique records.
events = {}
for record in parsed_records:
    event = record['event']
    events[event] = events.get(event, 0) + 1
print(events)

unqiue_users = set()
mulitple_events_users = set()
for record in parsed_records:
    if record['user_id'] in unqiue_users:
        mulitple_events_users.add(record['user_id'])
    unqiue_users.add(record['user_id'])
print(unqiue_users)
print(mulitple_events_users)
print("*" * 130)
# Problem 4: Test Case Management (List, Tuple, Dictionary)
# Scenario: You are given a list of test cases, each represented as a dictionary. You need to perform various operations for test management.

# Input:
# A list of dictionaries, where each dictionary represents a test case.
test_cases = [
    {"id": "TC001", "name": "Login valid credentials",
        "priority": "High", "status": "Passed", "tags": ["smoke", "ui"]},
    {"id": "TC002", "name": "Login invalid credentials", "priority": "Medium",
        "status": "Failed", "tags": ["smoke", "security"]},
    {"id": "TC003", "name": "User registration", "priority": "High",
        "status": "Not Run", "tags": ["regression", "ui"]},
    {"id": "TC004", "name": "Password reset flow",
        "priority": "High", "status": "Passed", "tags": ["security"]},
    {"id": "TC005", "name": "Search product", "priority": "Medium",
        "status": "Blocked", "tags": ["functional", "ui"]}
]
# Filtered by status="Passed", priority="High":
result = [test_case['id'] for test_case in test_cases if test_case['status']
          == "Passed" and test_case['priority'] == "High"]
print(result)
# Test Case Counts by Tag:
tag_count = {}
for test_case in test_cases:
    for tag in test_case['tags']:
        tag_count[tag] = tag_count.get(tag, 0)+1
print(tag_count)
tag_count

# Update Test Case Status: Given a test_case_id and new status,
# update the test case's status. If the test_case_id is not found, raise a ValueError.
def update_test_case_status(test_case_id, status):
    for test_case in test_cases:
        if test_case_id == test_case['id']:
            test_case['status'] = status
            return True
    raise ValueError(f"Test case with ID '{test_case_id}' not found.")

update_test_case_status("TC002", "Passed")
print(test_cases)
try:
    update_test_case_status("TC222", "Passed")
except ValueError as e:
    print(f"Error: {e}")

# Generate Test Run Summary: Return a dictionary summarizing the counts of test cases by their status
# (e.g., {'Passed': X, 'Failed': Y, ...}).
status_count = {}
for test_case in test_cases:
    status = test_case['status']
    status_count[status] = status_count.get(status, 0) + 1
print(status_count)

# Problem 5: Array/List Manipulation for Performance (List, Set, Tuple)
# Scenario: You are working with a large dataset represented as a list of integers, and need to perform efficient operations.
data = [1, 5, 2, 8, 5, 9, 1, 6, 2, 10, 5, 3]

# Find K-th Largest Element: Given the data list and an integer k, find the k-th largest element. 
# Do not sort the entire list if k is small (think about more efficient approaches).
k = 3
import heapq
pq = []
for num in data:
    heapq.heappush(pq, num)
    print(pq)
    if len(pq)> k:
        heapq.heappop(pq)
print(pq[0])

# Find Missing Numbers in Range: Given `data` and a `min_val`, `max_val` range (inclusive),
# find all integers within that range that are not present in `data`.
num_set = {num for num in data}
min_val = 1
max_value = 10
missing_numbers = [i for i in range(min_val, max_value+1) if i not in num_set]
print(missing_numbers)


# Find Pairs with a Specific Sum: Given `data` and a `target_sum`,
# find all unique pairs of numbers `(a, b)` from `data` such that `a + b = target_sum`.
# Each number can only be used once per pair.
target_sum=10
num_dict = {}
for num in data:
    num_dict[num] = num_dict.get(num, 0)+1

pairs = []
print(num_dict)
for num in num_dict:
    diff = target_sum - num
    if num_dict.get(diff, 0) > 0 and num_dict.get(num, 0) > 0:
        pairs.append((max(num, diff), min(num, diff)))
        num_dict[diff] -= 1
        num_dict[num] -= 1
print(num_dict)
print(pairs)