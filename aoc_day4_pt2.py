import re

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day4.txt'

#Part 1
card_dict = {}
num_copies = [1]*209
print(num_copies)

with open(file) as f:
    for ind, row in enumerate(f):
        print(row)
        parts = [word.strip() for word in re.split(r'[:|]', row)]
        gamenum = re.findall(r'\d+', parts[0])
        winlist = [int(num) for num in parts[1].split()]
        mylist = [int(num) for num in parts[2].split()]

        for j in range(1, num_copies[ind]+1):
            count = 1
            for ind2,num in enumerate(mylist):
                if(num in winlist):
                    num_copies[ind+count] +=1
                    count+=1




print('Part 1:', sum(num_copies))

