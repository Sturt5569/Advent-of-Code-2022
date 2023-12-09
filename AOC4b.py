file = open('Advent of Code 2022/aoc 4 input.txt')
count = 0
for line in file:
    ch1,ch2,ch3,ch4 = "","","",""
    marker = 1
    for ch in line:
        if ch.isdigit():
            if marker == 1:
                ch1 += ch
            if marker == 2:
                ch2 += ch
            if marker == 3:
                ch3 += ch
            if marker == 4:
                ch4 += ch
        if ch == "-" or ch == ",":
            marker += 1
    
    r1 = [i for i in range(int(ch1),int(ch2)+1)]
    r2 = [i for i in range(int(ch3),int(ch4)+1)]
    
    for r in r1:
        if r in r2:
            count +=1
            break
print(count)
file.close()