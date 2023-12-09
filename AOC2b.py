file = open('Advent of Code 2022/aoc 2 input.txt')
score = 0
for line in file:
    
    line = line.split()
    if line[1] == "X":
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 1
        else:
            score += 2
    if line[1] == "Y":
        score += 3
        if line[0] == "A":
            score += 1
        elif line[0] == "B":
            score += 2
        else:
            score += 3
    if line[1] == "Z":
        score += 6
        if line[0] == "A":
            score += 2
        elif line[0] == "B":
            score += 3
        else:
            score += 1
print(score)


file.close()