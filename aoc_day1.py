# AOC day 1
import re
#Read in txt file, for each line, get first and last digit

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day1.txt'

#Part 1
with open(file) as f:
    num_total = 0
    for row in f:
        nums = []
        for c in row:
            if c.isdigit(): nums.append(c)
        num_total = num_total + int(nums[0]+nums[-1])

print('Part 1:', num_total)

#Part 2
file2 = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day1.txt'

digs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digs_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


with open(file2) as f:
    num_total = 0
    for row in f:
        nums = []
        for ind,c in enumerate(row):
            if c.isdigit(): nums.append(str(c))
            for i in digs:
                if row[ind:ind+len(i)]==i:
                    nums.append(digs_dict[row[ind:ind+len(i)]])

        num_total = num_total + int(nums[0]+nums[-1])

print('Part 2:', num_total)


