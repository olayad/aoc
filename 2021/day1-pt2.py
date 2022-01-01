#!/usr/bin/env python3

test = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]

fp = open('2021/day1-pt2-input.txt')

increased = 0
decreased = 0
w1 = 0 
w2 = 0
w3 = 0
for index, reading in enumerate (fp):
    content = fp.readlines()

for index, line in enumerate(content):
    print(f'index:{index}, line{line}')
    print(f'line: {line}, content[index+0]:{content[index+0]} ,\
        content[index+1]: {content[index+1]}, \
        content[index+2]: {content[index+2]}')
    # for (i = 1; i == 3; i++)
        # print (fp[])
    if index == 5:
        exit(0)


    

print(f'Decreased: {decreased}')
print(f'Increased: {increased}')
