import re
import pandas as pd

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day6.txt'

with open(file) as f:
    entries = f.read()
    parts = entries.split('\n')
    times = [int(match) for match in re.findall(r'\d+', parts[0])]
    dists = [int(match) for match in re.findall(r'\d+', parts[1])]

total = 1
for i,j in zip(times, dists):
    count = 0
    for k in range(0, i):
        disp = k*(i-k)
        if disp>j: count +=1
    if count>0: total*= count

print(total)

#Part 2
#I was letting this run in the background while I worked on a more efficient way but it finished before I got there so here ya go

with open(file) as f:
    entries = f.read()
    parts = entries.split('\n')
    time = int((re.findall(r'\d+', parts[0].replace(" ", "")))[0])
    dist = int((re.findall(r'\d+', parts[1].replace(" ", "")))[0])

count = 0
for k in range(0, time):
    print((k/time)*100, '%')
    disp = k*(time-k)
    if disp>dist: count +=1

print('Answer:', count)


