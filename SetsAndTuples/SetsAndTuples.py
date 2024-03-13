#################################################################
##                            SET                              ##
#################################################################

# List  -> []
# Set   -> {}
# Tuple -> ()

# Declared using {}
# Can be changed
# Mutable

my_set = {1, 7, 3, 5, 6, 9, 8, 2, 4}
print(my_set)
print(len(my_set))

for i in my_set:
    print(i)

"""
Discard the element passed
"""
my_set.discard(3)
print(my_set)

"""
Difference of adding elements in a Set
"""
my_set.add(10)  # add a unique value to the set()
print(my_set)

my_set.update([11, 13, 56, 1231])  # add multiples values for the set()
print(my_set)  # to the end of set()

#################################################################
##                          TUPLES                             ##
#################################################################

# Declared using ()
# The value do not change
# Immutable


my_tuple = (1, 5, 3, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))

print(my_tuple.count(3))
print(my_tuple.index(4))
