file = open('Advent of Code 2022/aoc 6 input.txt')
chars = 0
set = []
for line in file:

    for i in range(4096):
        set.append(line[i])
        chars += 1
        if chars < 14:
            continue
        if chars > 14:
            set.pop(0)
        
        found = True
        for i in range(14):
            for j in range(14):
                if i==j:
                    continue
                if set[i] == set[j]:

                    found = False
        if found:
            print(set)
            print("Character:", chars)
            break

                    

file.close()