#!/usr/bin/env python3

test1 = ['00100',
         '11110',
         '10110',
         '10111',
         '10101',
         '01111',
         '00111',
         '11100',
         '10000',
         '11001',
         '00010',
         '01010']

test2 = ['000011001000',
         '001111100100',
         '110101011111',
         '010100001101',
         '110001001000']


def get_bit(value, position):
    return value[position]


size: int = 12
fp = open('../day3-input.txt')

gamma: str = '0b'
epsilon: str = '0b'
for index in range(size):
    count_0: int = 0
    count_1: int = 0
    for i in fp:
        value = get_bit(i, index)
        if value == '1':
            count_1 += 1
        if value == '0':
            count_0 += 1

    if count_0 > count_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    fp.seek(0)

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)
print(f'{gamma=} gamma:{gamma_int}')
print(f'{epsilon=} epsilon:{epsilon_int}')
print(f'res: {gamma_int * epsilon_int}')
