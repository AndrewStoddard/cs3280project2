#!/usr/bin/env python3

'''
Project 2
'''
import utils
import http_server

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"

def ipv6_subnet_calc(ipv6, prefix):
    """
    calculates the ipv6 subnet
    """
    ipv6_split = ipv6.split(':')
    active_hex = prefix // 16
    subnet = ipv6_split[active_hex]
    active_hex_bits = prefix % 16
    active_hex_index = active_hex_bits // 4
    active_bits = active_hex_bits % 4

    subnet_result = ""
    if subnet == "":
        subnet_result = "0000"
    else:
        for character_index, character in enumerate(subnet):
            if character_index > active_hex_index - 1:
                subnet_result += "0000"

            elif character_index <= active_hex_index - 1:
                hex_binary = utils.hex_to_binary(character)[2:]
                for bit in hex_binary:
                    if int(bit) & 1:
                        subnet_result += "1"
                    else:
                        subnet_result += "0"
            else:
                hex_binary = utils.hex_to_binary(character)[2:]
                for index, bit in enumerate(hex_binary):
                    if index < active_bits:
                        subnet_result += "0"
                    else:
                        if int(bit) & 1:
                            subnet_result += "1"
                        else:
                            subnet_result += "0"
    result = ""
    for index, hex_value in enumerate(ipv6_split):
        if index == active_hex:
            result += str(hex(int(subnet_result, 2)))[2:]
        elif index < active_hex:
            result += hex_value
        else:
            result += "0000"
        if index < len(ipv6_split) - 1:
            result += ":"

    return result






def ipv4_subnet_calc(ip_address, subnet_mask, is_subnet_mask_in_bits):
    '''
    calculates the ipv4 subnet
    '''


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
    return new_ip

def main(ip_address, subnet_mask):
    """
    Validates the Ip and mask passed in
    """
    error = 400
    if utils.is_valid_ipv6(ip_address):
        try:
            if int(subnet_mask) < 129:
                return ipv6_subnet_calc(ip_address, subnet_mask)
            else:
                print("Invalid Subnet Mask")
        except ValueError:
            print("Invalid Subnet Mask")
    elif utils.is_valid_ip(ip_address):
        if utils.is_valid_subnet_mask(subnet_mask):
            return ipv4_subnet_calc(ip_address, subnet_mask, False)

        try:
            if int(subnet_mask) < 32 and int(subnet_mask) > 0:
                return ipv4_subnet_calc(ip_address, subnet_mask, True)
            else:
                print("Invalid Subnet Mask")
        except ValueError:
            print("Invalid Subnet Mask")
    return error

if __name__ == "__main__":
    http_server.start_server()
