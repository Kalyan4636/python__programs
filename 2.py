# Write a Python program to check if lowercase letters exist in a string.

str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))
