# Rubber duck debugger
from collections import deque


def duck_type(total):
    duck = ""
    if 0 <= total <= 60:
        duck = "Darth Vader Ducky"
    elif 60 < total <= 120:
        duck = "Thor Ducky"
    elif 120 < total <= 180:
        duck = "Big Blue Rubber Ducky"
    elif 180 < total <= 240:
        duck = "Small Yellow Rubber Ducky"

    return duck


results = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

time_needed = deque(int(i) for i in input().split(" "))
tasks_per_programmer = deque(int(i) for i in input().split(" "))

while time_needed and tasks_per_programmer:
    curr_time = time_needed.popleft()
    curr_task = tasks_per_programmer.pop()
    curr_sum = curr_time * curr_task

    if curr_sum > 240:
        curr_task -= 2
        tasks_per_programmer.append(curr_task)
        time_needed.append(curr_time)
    else:
        curr_duck_type = duck_type(curr_sum)
        results[curr_duck_type] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{k}: {v}") for k, v in results.items()]
