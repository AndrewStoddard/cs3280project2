#!/usr/bin/env python3

'''
Project 2
'''
import sys
import utils

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"











def main(ip_address, subnet_mask):
    '''
    The main function
    '''
    is_subnet_mask_in_bits = False
    if not utils.is_valid_ip(ip_address):
        print("Invalid IP")

    if not utils.is_valid_subnet_mask(subnet_mask):
        try:
            if int(subnet_mask) < 32 and int(subnet_mask) > 0:
                is_subnet_mask_in_bits = True
            else:
                print("Invalid Subnet Mask")
                return
        except ValueError:
            print("Invalid Subnet Mask")
            return


    octets = ip_address.split('.')

    subnet_active_bits = utils.find_active_bits(subnet_mask, is_subnet_mask_in_bits)
    subnet_maxed_octets = utils.find_maxed_octets(subnet_mask, is_subnet_mask_in_bits)


    binary_of_active = utils.to_binary_from_active_bits(subnet_active_bits)
    binary_of_changing_octet = '0b' + bin(int(octets[subnet_maxed_octets]))[2:].zfill(8)
    binary_list_of_active = utils.convert_binary_string_to_list(binary_of_active)
    binary_list_of_changing_octet = utils.convert_binary_string_to_list(binary_of_changing_octet)

    new_binary_for_changing = '0b'
    for i in range(0, 8):
        if int(binary_list_of_active[i]) & int(binary_list_of_changing_octet[i]):
            new_binary_for_changing += '1'
        else:
            new_binary_for_changing += '0'
    changed_octet = utils.convert_binary_to_dec(new_binary_for_changing)

    new_ip = ''
    for octet in octets:
        if octets.index(octet) < subnet_maxed_octets:
            new_ip += octet + '.'
        elif octets.index(octet) == subnet_maxed_octets:
            new_ip += str(changed_octet)
        else:
            new_ip += '.0'



    print(new_ip)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
