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

for index, reading in enumerate (fp):
    content = fp.readlines()

window_sum, increased, decreased, prev, cur = 0, 0, 0, 0, 0
# for index, line in enumerate(content):
for index, line in enumerate(test):
    window_sum = content[index+0] + content[index+1] + content[index+2]

    print(f'\nindex:{index}, line{line}')
    print(f'window_sum:{window_sum}, content[index+0]:{content[index+0]}, content[index+1]: {content[index+1]},content[index+2]: {content[index+2]}')

    if index == 0:
        prev = window_sum
        continue

    if prev < window_sum:
        increased += 1
    elif prev > window_sum:
        decreased += 1
    else:
        print(f'????? prev:{prev}, window_sum:{window_sum}')
    
    if index == (len(content) - 3):
        print(f'end of the rope...')
        break


    prev = window_sum


    # if index == 5:u
    #     print(f'Index is 5')
    #     exit(0)

print(f'Decreased: {decreased}')
print(f'Increased: {increased}')
