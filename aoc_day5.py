import re
import pandas as pd

file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day5.txt'

with open(file, 'r') as f:
    entries = f.read()
    entries = entries.strip()
    parts = entries.split("\n\n")
    seeds = [int(seed) for seed in parts[0].split(":")[-1].strip().split()]
    parts = parts[1:]


partsmap = {}
for i in parts:
    rows = i.split('\n')
    items = [item.replace(":", "") for item in re.split('[- ]', rows[0])]
    rows = rows[1:]
    source = items[0]
    dest = items[2]
    sub_df = pd.DataFrame(columns = [source, dest])
    vec1 = []
    vec2 = []
    for row in rows:
        row = [int(piece) for piece in row.split(" ")]
        vec1.append([row[1], row[1] + row[2]])
        vec2.append([row[0], row[0] + row[2]])

    sub_df[source] = vec1
    sub_df[dest] = vec2

    partsmap[source + dest] = sub_df


# Okay so now we have a dict that has each pair of values, and within each pair of values a df showing the mapping between them (unless they are equal)

#Now I want to go into locations and find the minimum, and work back from there
# So that means go into location, find min, find humidity, go into temphumidity, find temp

#minlocation = 0
#i =0
#while i ==0:
locations = []
for i in seeds:
    searchval= i
    print('Seed:', i)
    for key, value in (partsmap.items()):
        this_df = partsmap[key]
        for index, j in enumerate(this_df.iloc[:,0]):
            if j[0] <= searchval <= j[1]:
                target = this_df.iloc[:,1][index]
                searchval = target[0] + (searchval-j[0])
                break
    locations.append(searchval)
        # newval = this_df.iloc[:, 0].values[this_df.iloc[:, 1] == searchval]
        # if newval:
        #     searchval = newval[0]

    #if(searchval in seeds): i=1
    #minlocation += 1


print('location:', min(locations))


















