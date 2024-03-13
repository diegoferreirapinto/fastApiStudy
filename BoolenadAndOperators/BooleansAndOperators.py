"""
Booleans and Operators
"""

# Booleans
like_coffe = True
like_tea = False
variable1 = 'False'
variable2 = 0

print(type(like_coffe))
print(type(like_tea))
print(type(variable1))
print(type(variable2))

# Operators

## Comparison

print(f"1 == 2 ? {1 == 2}")  # equal to
print(f"1 != 2 ? {1 != 2}")  # not equal
print(f"1 > 2 ? {1 > 2}")  # greater than
print(f"1 < 2 ? {1 < 2}")  # less than
print(f"1 >= 2 ? {1 >= 2}")  # greater than or equal to
print(f"1 >= 1 ? {1 >= 1}")  # greater than or equal to
print(f"1 <= 1 ? {1 <= 1}")  # less than or equal to
print(like_coffe == True)

## Logical
print(f"1 > 1 and 1 == 1 ? {1 > 1 and 1 == 1}")  # output: False
print(f"1 >= 1 and 5 != 8 ? {1 >= 1 and 5 != 8}")  # output: True
print(f"1 >= 1 and 5 > 8 ? {1 >= 1 or 5 > 8}")  # output: True
print(f"1 > 1 and True == False ? {1 > 1 or True == False}")  # output: False
print(f"NOT (1 > 1 and True == False) ? {not(1 > 1 or True == False)}")  # output: True - logical inverter