file = open('Advent of Code 2022/aoc 7 input.txt')

disk = {}

ls = False
current_dir = []
dest = 0

for line in file:  
    if line == "$ cd /":
        continue                
    if "$" in line:
        line = line.split()
        if line[1] == "cd":
            if line[2] != "..":
                current_dir.append([line[2]])
                #current_dir[0].append({})
            else:
                current_dir.pop()

        if line[1] == "ls":
            ls = True
            target = current_dir[-1]
            size = 0
        if line[0].isdigit() and ls == True:
            size += int(line[0])
            print("digits")
        
    
    print(current_dir)

            
file.close()