#!/usr/bin/env python3

'''
Project 2
'''
import sys

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"


def find_subnet_number(bits):
    maxed_intervals = bits // 8
    last_on_bits = bits % 8
    subnet_number = ""
    for i in range(0, maxed_intervals):
        subnet_number += '255.'
    binary = []
    for i in range(0, 8):
        if (i < last_on_bits):
            binary.append('1')
        else:
            binary.append('0')
    value = convert_binary_to_dec(binary)
    subnet_number += str(value)
    inactive_intervals = 4 - maxed_intervals
    for i in range(1, inactive_intervals):
        if (i < inactive_intervals):
            subnet_number += ".0"

    return subnet_number

def convert_binary_to_dec(binary):
    value = 0
    for i in range(len(binary)):
        digit = binary.pop()
        if (digit == '1'):
            value = value + pow(2, i)
    return value

def main(arg1):
    '''
    The main function
    '''
    print(find_subnet_number(int(arg1)))


if __name__ == "__main__":
    main(sys.argv[1])