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

for line in file:
    rucksack = []
    digs = int((len(line) - 1)/2)

    s1 = line[:digs]
    s2 = line[digs:]

    for ch in s1:
        if ch in s2:
            rucksack.append(ch)
    for item in rucksack:
        if item in upper:
            value = upper.get(item)
        if item in lower:
            value = lower.get(item)
    total += value
print(total)
file.close()