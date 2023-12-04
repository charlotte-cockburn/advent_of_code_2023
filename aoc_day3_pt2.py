import pandas as pd
import numpy as np

def check_sym(df, i, j):
    width = df.shape[1]
    height = df.shape[0]
    symbols = ['*']
    #West
    asterisk_list = []
    if(j>0):
        if(df.iloc[i, j-1] in symbols): asterisk_list.append([i, j-1])
    #Southwest
    if((j>0) & (i<height-1)):
        if(df.iloc[i+1, j-1] in symbols): asterisk_list.append([i+1, j-1])
    #South
    if(i<height-1):
        if(df.iloc[i+1, j] in symbols): asterisk_list.append([i+1, j])
    #Southeast
    if((j<width-1) & (i<height-1)):
        if(df.iloc[i+1, j+1] in symbols): asterisk_list.append([i+1, j+1])
    #East
    if((j<width-1)):
        if(df.iloc[i, j+1] in symbols): asterisk_list.append([i, j+1])
    #Northeast
    if((j<width-1) & (i>0)):
        if(df.iloc[i-1, j+1] in symbols): asterisk_list.append([i-1, j+1])
    #North
    if(i>0):
        if(df.iloc[i-1, j] in symbols): asterisk_list.append([i-1, j])
    #Northwest
    if((i>0) & (j>0)):
        if(df.iloc[i-1, j-1] in symbols): asterisk_list.append([i-1, j-1])

    return asterisk_list



file = 'C:\\Users\\CockburnC\\Documents\\AdventOfCode_2023\\aoc_day3.txt'
df = pd.read_fwf(file, widths = [1]*140, header = None)
print(df)


# i = col number (y-axis)
# j = row number (x-axis)
for i in range(0, df.shape[1]):
    for j in range(0, df.shape[0]):
        try:
            df.iloc[i,j] = int(df.iloc[i,j])
        except:
            continue

width = df.shape[1]
height = df.shape[0]
ast_df = pd.DataFrame([[[] for _ in range(height)] for _ in range(width)])
engsum = []
i = 0
while i < height:
    j = 0
    while j < width:
        val = df.iloc[i,j]
        #if it's a number
        if(isinstance(val, int)):
            #if it's on the righthand edge
            if(j == width):
                val2 = '.'
                val3 = '.'
            #if it's one less than the edge
            elif((j == width-1)):
                val2 = df.iloc[i,j+1]
                val3 = '.'
            #otherwise
            else:
                val2 = df.iloc[i,j+1]
                val3 = df.iloc[i,j+2]

            #print(val, val2, val3)
            #NOW: check if it's one, two, or three digit number
            #3 digits
            if((isinstance(val2, int)) & (isinstance(val3, int))):
                num = int(str(val) + str(val2) + str(val3))
                sym1 = check_sym(df, i,j)
                sym2 = check_sym(df,i,j+1)
                sym3 = check_sym(df, i, j+2)

                unique_ast = set()
                for sublist in sym1+sym2+sym3:
                    unique_ast.add(tuple(sublist))
                result = [list(sublist) for sublist in unique_ast]
                print(result)

                for index in result:
                    ast_df.iloc[index[0], index[1]].append(num)
                j += 3
            elif((isinstance(val2, int))):
                num = int(str(val)+str(val2))
                sym1 = check_sym(df,i,j)
                sym2 = check_sym(df,i,j+1)

                unique_ast = set()
                for sublist in sym1+sym2:
                    unique_ast.add(tuple(sublist))
                result = [list(sublist) for sublist in unique_ast]
                print(result)

                for index in result:
                    ast_df.iloc[index[0], index[1]].append(num)


                j += 2
            else:
                num = val
                sym1 = check_sym(df,i,j)
                unique_ast = set()
                for sublist in sym1:
                    unique_ast.add(tuple(sublist))
                result = [list(sublist) for sublist in unique_ast]
                print(result)

                for index in result:
                    ast_df.iloc[index[0], index[1]].append(num)

                j+=1

        else: j +=1
    i +=1

width = ast_df.shape[1]
height = ast_df.shape[0]
engsum = []
i = 0
while i < height:
    j = 0
    while j < width:
        this_list = ast_df.iloc[i,j]
        if(len(this_list)==2):
            engsum.append(this_list[0]*this_list[1])
        j+=1
    i+=1


print('Part 2: ', sum((engsum)))





