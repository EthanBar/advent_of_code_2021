with open("Day_01/input.txt", 'r') as input_file:
    input = input_file.read()

depths = [int(line) for line in input.splitlines()]
inc_1 = inc_2 = 0

for i in range(len(depths) - 1): inc_1 += depths[i + 1] > depths[i]
for i in range(len(depths) - 3): inc_2 += sum(depths[i + 1:i + 4]) > sum(depths[i:i + 3])

print(f"Part 1: {inc_1} \nPart 2: {inc_2}")