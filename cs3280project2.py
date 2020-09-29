#!/usr/bin/env python3

'''
Project 2
'''
import sys
import re

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"

subnet_maxed_octets = 0
subnet_active_bits = 0

def isValidOctet(octet):
    regex = re.compile(r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")
    if regex.match(octet):
        return True
    return False

def find_maxed_octets(subnet_mask):
    if (not isValidOctet(subnet_mask)):
        try:
            if (int(subnet_mask) < 32 and int(subnet_mask) > 0):
                return int(subnet_mask) // 8
            else:
                print("Invalid Subnet Mask")
                return
        except:
            print("Invalid Subnet Mask")
            return
    else: 
        return len(re.findall(re.compile(r"255"), subnet_mask))

def find_active_bits(subnet_mask):
    if (not isValidOctet(subnet_mask)):
        try:
            if (int(subnet_mask) < 32 and int(subnet_mask) > 0):
                return int(subnet_mask) % 8
            else:
                print("Invalid Subnet Mask")
                return
        except:
            print("Invalid Subnet Mask")
            return
    else: 
        octets = subnet_mask.split('.')
        active_octet = ''
        for octet in octets:
            if (not octet == '255' and not octet == '0'):
                active_octet = octet
        if active_octet == '':
            active_octet = '0'
        active_binary = bin(int(active_octet))
        return count_active_bits(active_binary)

def count_active_bits(binary):
    binary = binary.replace('0b', '')
    count = 0
    for bit in binary:
        if bit == '1':
            count += count + 1
    return count

        
def find_subnet_number(bits):
    subnet_number = ''
    for i in range(0, subnet_maxed_octets):
        subnet_number += '255.'
    binary = get_binary_for_8_bits(subnet_active_bits)
    value = convert_binary_to_dec(binary)
    subnet_number += str(value)
    inactive_intervals = 4 - subnet_maxed_octets
    for i in range(1, inactive_intervals):
        if (i < inactive_intervals):
            subnet_number += '.0'

    return subnet_number

def convert_binary_string_to_list(binary):
    binary = binary.replace('0b', '')
    print(binary)
    binary_list = []
    for letter in binary:
        binary_list.append(letter)
    return binary_list

def get_binary_for_8_bits(number_of_active_bits):
    binary = "0b"
    for i in range(0, 8):
        if (i < number_of_active_bits):
            binary += '1'
        else:
            binary += '0'
    return binary

def convert_binary_to_dec(binary):
    binary_list = convert_binary_string_to_list(binary)
    value = 0
    for i in range(len(binary_list)):
        digit = binary_list.pop()
        if (digit == '1'):
            value = value + pow(2, i)
    return value

def main(arg1, arg2):
    '''
    The main function
    '''
    subnet_active_bits = find_active_bits(arg2)
    subnet_maxed_octets = find_maxed_octets(arg2)
    octets = arg1.split('.')
    
    binary_of_active = get_binary_for_8_bits(subnet_active_bits)
    binary_of_changing_octet = bin(int(octets[subnet_maxed_octets]))[2:].zfill(8)
    print("binco" + binary_of_changing_octet)
    binary_list_of_active = convert_binary_string_to_list(binary_of_active)
    binary_list_of_changing_octet = convert_binary_string_to_list(binary_of_changing_octet)
    
    new_binary_for_changing = '0b'
    for i in range(0, 8):
        if (int(binary_list_of_active[i]) & int(binary_list_of_changing_octet[i])):
            new_binary_for_changing += '1'
        else:
            new_binary_for_changing += '0'
    changed_octet = convert_binary_to_dec(new_binary_for_changing)

    new_ip = ''
    for octet_index in range(0, len(octets)):
        if (octet_index < subnet_maxed_octets):
            new_ip += octets[octet_index] + '.'
        elif (octet_index == subnet_maxed_octets):
            new_ip += str(changed_octet)
        else:
            new_ip += '.0'
    print(new_ip)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])