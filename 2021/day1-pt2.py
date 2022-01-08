#!/usr/bin/env python3

test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

fp = open('./day1-pt2-input.txt')
content = fp.readlines()

window_sum, equal, increased, decreased, prev, cur = 0, 0, 0, 0, 0, 0
for index, line in enumerate(content):
    window_sum = int(content[index+0]) + int(content[index+1]) + int(content[index+2])
    if index == 0:
        prev = window_sum
        continue
    if prev < window_sum:
        increased += 1
    elif prev > window_sum:
        decreased += 1
    elif prev == window_sum:
        equal += 1
        continue
    else:
        print(f'Dont know what happened?')
    if index == (len(content) - 3):
        break

    prev = window_sum

print(f'\tDecreased: {decreased}')
print(f'\tIncreased: {increased}')
print(f'\tEqual: {equal}')
# print(f'\tTotal:{decreased + increased + equal}')
# print(f'\tContent len: {len(content)}')
