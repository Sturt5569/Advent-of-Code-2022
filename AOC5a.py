file = open('Advent of Code 2022/aoc 5 input.txt')
stk = [[],
        ["B","S","V","Z","G","P","W"],      # Stack 1
        ["J","V","B","C","Z","F"],          # Stack 2
        ["V","L","M","H","N","Z","D","C"],  # Stack 3
        ["L","D","M","Z","P","F","J","B"],  # Stack 4
        ["V","F","C","G","J","B","Q","H"],  # Stack 5
        ["G","F","Q","T","S","L","B"],      # Stack 6
        ["L","G","C","Z","V"],              # Stack 7
        ["N","L","G"],                      # Stack 8
        ["J","F","H","C"]                   # Stack 9
       ]

def move(count,src,dst):
    for i in range(int(count)):
        temp = stk[int(src)].pop()
        stk[int(dst)].append(temp)


for line in file:
    line = line.split()
    if len(line) > 0:
        if line[0] == "move":
            move(line[1],line[3],line[5])
            
        
for s in stk:
    if s == "":
        continue
    print(s)
file.close()