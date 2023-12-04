import re

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day4.txt'

#Part 1
winsum = []
with open(file) as f:
    for row in f:
        parts = [word.strip() for word in re.split(r'[:|]', row)]
        winlist = [int(num) for num in parts[1].split()]
        mylist = [int(num) for num in parts[2].split()]

        score = 0
        for num in mylist:
            if((score == 0) & (num in winlist)):
                score = 1
            elif(num in winlist):
                score = score*2

        winsum.append(score)

print('Part 1:', sum(winsum))

