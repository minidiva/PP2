#list 
list = ['a', 'b', 'c']
#
# Indexation starts with 0
# Lists are changeable
# Lists can have duplicates
# len() - length
# Lists can have any data type
# type()
# list() constructor

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

print(list[0]) # a
print(list[-1]) # c
print(list[1:2]) # b
# etc.

thislist = ['a', 'b', 'c']
if 'a' in thislist:
    print('\'a\' is in the list')
