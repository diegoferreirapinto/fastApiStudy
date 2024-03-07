days_until_birth = input("How many days before your birthday? ")
#
# We can make an explicit parse on the INPUT, not only on
#days_until_birth = int(input("How many days before your birthday? "))
#
#We can round a number value to approximate number
#print(round(days_until_birth/7,2)) -> how many decimal plates we want,
#                                      in this case is 2
#
#convert_days_in_weeks = (int(days_until_birth) % 7)

if (int(days_until_birth) % 7 == 0):
    weeks = (int(days_until_birth) // 7)
    print(f"{weeks} weeks to your birthday")
else:
    weeks = (int(days_until_birth) // 7)
    days_left = (int(days_until_birth) % 7)
    print(f"{weeks} weeks and {days_left} days to your birthday")


## type() is a function to verify the type of variable

