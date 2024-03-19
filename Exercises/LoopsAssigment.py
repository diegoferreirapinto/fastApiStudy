my_list = ["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday"]

max_repeat = 0
while max_repeat < 3:
    print(f"{max_repeat} -> {my_list}")
    max_repeat += 1

loop_idx = 0
for loop_idx in my_list:
    # match loop_idx:
    #     case 'Monday':
    #         print('Segunda!!')
    #     case _:
    #         print('Default Case')
    if loop_idx == 'Saturday':
        continue
    elif loop_idx == 'Tuesday':
        continue

    print(loop_idx)

