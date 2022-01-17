#!/usr/bin/env python3

test = ['forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2']

fp = open('../day2-input.txt')

horizontal: int = 0
depth: int = 0
for i in fp:
    direction = i.split(' ')[0].strip('\n')
    distance = int(i.split(' ')[1])
    # print(f'{i=}, {direction=}, {distance=}')
    if direction == 'forward':
        horizontal += distance
    elif direction == 'down':
        depth += distance
    elif direction == 'up':
        depth -= distance
    else:
        print(f'Instruction unclear???')

print(f'{horizontal=}, {depth=}, total: {horizontal*depth}')








