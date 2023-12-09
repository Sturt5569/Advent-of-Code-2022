file = open('Advent of Code 2022/aoc 1 input.txt')

elf_total = 0
elves = []
for line in file:
    if line != "\n":
        elf_total += int(line)
    else:
        elves.append(elf_total)
        elf_total = 0

max_val = 0
for elf in elves:
    if elf > max_val:
        max_val = elf

print(max_val)
file.close()