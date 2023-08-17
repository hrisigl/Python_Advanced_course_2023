from collections import deque

armor = deque(int(i) for i in input().split(","))
impact = deque(int(i) for i in input().split(","))

killed_monsters = 0

while armor and impact:
    curr_armor = armor.popleft()
    curr_strike = impact.pop()

    if curr_strike >= curr_armor:
        curr_strike -= curr_armor
        killed_monsters += 1

        if curr_strike > 0 and impact:
            impact[-1] += curr_strike
        elif curr_strike > 0 and not impact:
            impact.append(curr_strike)

    else:
        curr_armor -= curr_strike
        armor.append(curr_armor)

if not armor:
    print("All monsters have been killed!")
if not impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
