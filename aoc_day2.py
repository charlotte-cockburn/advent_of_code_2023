import re

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day2.txt'

#Part 1
gamesum = 0
with open(file) as f:
    for row in f:
        parts = [word.strip() for word in re.split(r'[:;,]', row)]
        gamenum = int(re.findall(r'\d+', parts[0])[0])
        addgame = True
        for part in parts:
            num = int(re.findall(r'\d+', part)[0])
            if (('blue' in part) & (num>14)) | (('green' in part) & (num>13)) | (('red' in part) & (num > 12)):
                addgame = False
                break
        if(addgame): gamesum += gamenum

print('Part 1:', gamesum)

#Part 2
gamesum = 0
with open(file) as f:
    for row in f:
        minred, minblue, mingreen = [0, 0, 0]
        parts = [word.strip() for word in re.split(r'[:;,]', row)]
        for part in parts:
            num = int(re.findall(r'\d+', part)[0])
            if (('blue' in part) & (num>minblue)): minblue = num
            elif (('red' in part) & (num>minred)): minred = num
            elif (('green' in part) & (num>mingreen)): mingreen = num
        gamesum += minblue*minred*mingreen

print('Part 2:', gamesum)

