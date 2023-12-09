file = open('Advent of Code 2022/aoc 1 input.txt')

elf_total = 0
elves = []
for line in file:
    if line != "\n":
        elf_total += int(line)
    else:
        elves.append(elf_total)
        elf_total = 0

print(elves)
elves.sort(reverse=True)

print(sum(elves[:3]))
file.close()