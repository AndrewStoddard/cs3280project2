'''
Utilities to assist in finding subnets based on an ip and mask.
'''

import re

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"

def is_valid_ip(ip_address):
    '''
    Checks if IP is valid
    '''
    regex = re.compile(r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")
    if regex.match(ip_address):
        return True
    return False

def is_valid_subnet_mask(subnet_mask):
    '''
    Checks if a subnet is valid
    '''
    octets = ['0', '128', '192', '224', '240', '248', '252', '254']

    subnet_mask_octets = subnet_mask.split(".")
    has_to_be_0 = False
    for octet in subnet_mask_octets:

        if octet == '255' and not has_to_be_0:
            pass
        elif octet in octets and not has_to_be_0:
            has_to_be_0 = True
        elif (not octet == '0' and has_to_be_0) or octet > '255':
            return False
        elif len(subnet_mask_octets) < 4:
            return False
    return True

def convert_binary_string_to_list(binary):
    '''
    Converts a binary value from a string to a list
    '''
    binary = binary.replace('0b', '')
    binary_list = []
    for letter in binary:
        binary_list.append(letter)
    return binary_list

def convert_binary_to_dec(binary):
    '''
    Converts a binary value from a string to a decimal
    '''
    binary_list = convert_binary_string_to_list(binary)
    value = 0
    for i in range(len(binary_list)):
        digit = binary_list.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value

def to_binary_from_active_bits(number_of_active_bits):
    '''
    Takes active bits(1s) and converts them to binary
    '''
    binary = "0b"
    for i in range(0, 8):
        if i < number_of_active_bits:
            binary += '1'
        else:
            binary += '0'
    return binary


def count_active_bits(binary):
    '''
    Counts the active bits(1s)
    '''
    binary = binary.replace('0b', '')
    count = 0
    for bit in binary:
        if bit == '1':
            count += 1
    return count

def find_maxed_octets(subnet_mask, bit_form):
    '''
    Finds the octest that are 255
    '''
    result = 0
    if bit_form:
        result = int(subnet_mask) // 8
    else:
        result = len(re.findall(re.compile(r"255"), subnet_mask))
    return result

def find_active_bits(subnet_mask, bit_form):
    '''
    Finds the active bits for the last octet not 0 if any previous were not 0 or 255
    '''
    result = 0
    if bit_form:
        result = int(subnet_mask) % 8
    else:
        subnet_mask_octets = subnet_mask.split('.')
        active_octet = ''
        last_octet = ''
        for octet in subnet_mask_octets:
            if not octet == '255' and not octet == '0':
                active_octet = octet
            last_octet = octet
        if active_octet == '':
            active_octet = last_octet
        active_binary = bin(int(active_octet))
        result = count_active_bits(active_binary)
    return result
