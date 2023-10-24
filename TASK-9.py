#!/usr/bin/env python
# coding: utf-8

# In[3]:


""" 1. What is the expected output of the following Python code given below-
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))"""

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))


# In[21]:


# 2. Write a Python code using Lambda function to check every element of a List is an Integer or String?

my_list = [1, 'two', 3, 'four', 5]

check_type = lambda x: isinstance(x, (int, str))

result = all(map(check_type, my_list))
print(result)


# In[13]:


# 3. Using the Python Lambda function create a Fibonacci series from 1 to 50 elements?

def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

fib_series = fibonacci(50)
print(fib_series)


# In[19]:


""" 4. Write a Python function to validate the Regular Expression for the following-

a) Email Address
b) Mobile numbers of Bangladesh
c) Telephone numbers of USA
d) 16 character Alpha-Numeric password composed of alphabets of Upper Case, Lower Case, Special Characters, Numbers."""

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_bangladesh_mobile_number(number):
    pattern = r'^\+880-1[1-9]\d{8}$'
    return bool(re.match(pattern, number))

def validate_usa_telephone_number(number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, number))

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

print(validate_email('example@example.com'))
print(validate_bangladesh_mobile_number('+880-1712345678'))
print(validate_usa_telephone_number('123-456-7890'))
print(validate_password('Akjdkfk231w2@$%&'))

