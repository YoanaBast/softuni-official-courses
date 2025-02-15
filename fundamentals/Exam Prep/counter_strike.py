
def battles(energy: int):
    battles_won = 0
    while True:
        command = input()

        if battles_won % 3 == 0:
            energy += battles_won

        if command == "End of battle":
            return f"Won battles: {battles_won}. Energy left: {energy}"
            break
        distance = int(command)

        if energy >= distance:
            battles_won += 1
            energy -= distance
        else:
            return f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy"

energy_inp = int(input())

print(battles(energy_inp))




