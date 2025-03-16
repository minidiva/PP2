import time
import math


# 1
def multiply_list(numbers):
    return math.prod(numbers)

numbers = [2, 3, 4, 5]
print("Task 1")
print("Product of list:", multiply_list(numbers))


# 2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

s = "Hello World!"
upper, lower = count_case(s)
print("Task 2")
print("Upper case letters:", upper)
print("Lower case letters:", lower)

# 3
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

string = "madam"
string1 = "ab"
print("Task 3")
print(f"Is '{string}' a palindrome?", is_palindrome(string))
print(f"Is '{string1}' a palindrome?", is_palindrome(string1))

# 4
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)


number = 25100
delay = 2123
result = delayed_sqrt(number, delay)
print("Task 4")
print(f"Square root of {number} after {delay} milliseconds is {result}")

# 5
def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
print("Task 5")
print(f"Are all elements in {tuple1} true? {all_elements_true(tuple1)}")
print(f"Are all elements in {tuple2} true? {all_elements_true(tuple2)}")