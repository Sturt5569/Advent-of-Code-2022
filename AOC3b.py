file = open('Advent of Code 2022/aoc 3 input.txt')
lower = {}
upper = {}
lett = "a"
let = "A"
total = 0

for i in range(26):
    lower.update({lett:i+1})
    upper.update({let:i+27})
    lett = chr(ord(lett)+1)
    let = chr(ord(let)+1)
group = []

for line in file:
    if len(group) <2:
        group.append(line)
    else:
        group.append(line)
        print(group)
        for ch in group[0]:
            if ch in group[1] and ch in group[2]:
                print(ch)
                if ch in upper:
                    value = upper.get(ch)
                if ch in lower:
                    value = lower.get(ch)
        total += value
        group = []
print(total)
file.close()