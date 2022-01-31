#!/usr/bin/env python3

test = [bin(0b00100),
        bin(0b11110),
        bin(0b10110),
        bin(0b10111),
        bin(0b10101),
        bin(0b01111),
        bin(0b00111),
        bin(0b11100),
        bin(0b10000),
        bin(0b11001),
        bin(0b00010),
        bin(0b01010)]


# fp = open('../day3-input.txt')
def get_bit(val, position):
        return val[2:].zfill(5)[position]


for i in test:

