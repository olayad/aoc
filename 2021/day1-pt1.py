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

fp = open('2021/day1-input.txt')

increased = 0
decreased = 0
prev = 0 
for index, reading in enumerate (fp):
    depth = int(reading)
    print(f'index: {index}, depth:{depth}')
    print(f'type index{type(index)}, type depth{type(depth)}')
    if index == 0:
        depth = prev
    else:
        if depth > prev:
            increased += 1
        elif depth < prev:
            decreased += 1
        else:
            print(f'whooops index{index}, prev: {prev} ,depth {dept}')
    prev = depth

print(f'Decreased: {decreased}')
print(f'Increased: {increased}')
