file = open('Advent of Code 2022/aoc 2 input.txt')
score = 0
for line in file:
    
    line = line.split()
    if line[1] == "X":
        score += 1
        if line[0] == "A":
            score += 3
        elif line[0] == "C":
            score += 6
    if line[1] == "Y":
        score += 2
        if line[0] == "B":
            score += 3
        elif line[0] == "A":
            score += 6
    if line[1] == "Z":
        score += 3
        if line[0] == "C":
            score += 3
        elif line[0] == "B":
            score += 6
print(score)


file.close()