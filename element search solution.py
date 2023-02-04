# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean.

# find is a function that takes an ordered list of numbers and another number,
# returning true or false whether the element appears in the list
# 
# l is a list ordered from smallest to largest
# element is the number to find in the original list
def find(ordered_list, element_to_find):
  for element in ordered_list:
    if element == element_to_find:
      return True
  return False
  
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True