"""
List are a collection of data
"""

my_list = [10, 32, 13, 48, 5]

people_list = ['Diego', 'Benjamin', 'Marcos']
print(people_list[1])

# We can get the last element using negative index
# No matter how big is the list, take a look on the
# example below. Pay attention, the index, when u
# use a negative index, starts with 1, in this case
# minus 1 (-1)

people_list = ['Diego', 'Benjamin', 'Marcos']
print(people_list[-3])

# We can use function LEN to verify the size of a list
print(len(people_list))

# Other way to print an interval of data is using :
# take a look

print(people_list[0:2])

# The print will start at the element 0
# will print the first name (idx 0), the second (1) but the last
# one will not be printed because is not inclusive

"""
Insert and Delete in a list
"""

# We use APPEND to INCLUDE in the list at the end of the list

people_list.append('Albino')
print(people_list)

# Or we can ADD in a specific index some information as we can use
# the code below with INSERT

people_list.insert(0,'Lenice')
print(people_list)

# But if we do not want to ADD some data, we can remove this data with
# REMOVE function, to remove an specific data or we can just use POP function
# to delete using de INDEX. See the code.

people_list.remove('Diego')
print(people_list)

people_list.pop(-1)
print(people_list)

# We can SORT an array (list), for example

people_list.sort()
print(people_list)

my_list.sort()
print(my_list)