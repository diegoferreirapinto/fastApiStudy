""""
For and While loops
"""

### FOR

list = [1, 2, 3, 4, 5, 6]

for iter in list:
    print(iter)

print("-----------------")

for iter in range(3, 6):
    print(iter)

### WHILE

print("vvv WHILE LOOPS vvv")

i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue  # break the loop and continue to another one
    print(i)
    if i == 4:
        break  # break the while loop
else:
    print("Bigger or equals than 5")
