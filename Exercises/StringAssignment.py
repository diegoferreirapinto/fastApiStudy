days_until_birth = input("How many days before your birthday? ")
#convert_days_in_weeks = (int(days_until_birth) % 7)

if (int(days_until_birth) % 7 == 0):
    weeks = (int(days_until_birth) // 7)
    print(f"{weeks} weeks to your birthday")
else:
    weeks = (int(days_until_birth) // 7)
    days_left = (int(days_until_birth) % 7)
    print(f"{weeks} weeks and {days_left} days to your birthday")



