with open("Day_02/input.txt", 'r') as input_file:
    input = input_file.read()

instructions = [line.split() for line in input.splitlines()]
position = depth = aim = 0

for instruction in instructions:
    if instruction[0] == "forward":
        position += int(instruction[1])
        depth += int(instruction[1]) * aim
    else:
        aim += int(instruction[1]) * (1 if instruction[0] == "down" else -1)

print(f"Part 1: {position * aim} \nPart 2: {position * depth}")