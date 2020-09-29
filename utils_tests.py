#!/usr/bin/env python3

import unittest
import utils

__author__ = "AndrewStoddard"
__version__ = "Fall 2020"

class TheUtilTestClass(unittest.TestCase):
    def testValidIP(self):
        result = utils.is_valid_ip('192.22.123.1')
        self.assertTrue(result)

    def testInvalidIPSlot1(self):
        result = utils.is_valid_ip('1920.251.123.1')
        self.assertFalse(result)

    def testInvalidIPSlot2(self):
        result = utils.is_valid_ip('192.256.123.1')
        self.assertFalse(result)

    def testInvalidIPSlot3(self):
        result = utils.is_valid_ip('192.256.1')
        self.assertFalse(result)
    
    def testInvalidIPSlot4(self):
        result = utils.is_valid_ip('192.256.1.')
        self.assertFalse(result)

    def testValidSubnetMaskSlot1(self):
        result = utils.is_valid_subnet_mask('192.0.0.0')
        self.assertTrue(result)
    
    def testValidSubnetMaskSlot2(self):
        result = utils.is_valid_subnet_mask('255.192.0.0')
        self.assertTrue(result)

    def testValidSubnetMaskSlot3(self):
        result = utils.is_valid_subnet_mask('255.255.192.0')
        self.assertTrue(result)

    def testValidSubnetMaskSlot4(self):
        result = utils.is_valid_subnet_mask('255.255.255.192')
        self.assertTrue(result)
   
    def testInvalidSubnetMaskSlot1(self):
        result = utils.is_valid_subnet_mask('0.255.255.192')
        self.assertFalse(result)

    def testInvalidSubnetMaskSlot2(self):
        result = utils.is_valid_subnet_mask('255.0.255.192')
        self.assertFalse(result)

    def testInvalidSubnetMaskSlot3(self):
        result = utils.is_valid_subnet_mask('255.255.0.192')
        self.assertFalse(result)

    def testInvalidSubnetMaskSlot4(self):
        result = utils.is_valid_subnet_mask('255.255.255.300')
        self.assertFalse(result)

    def testInvalidSubnetMask(self):
        result = utils.is_valid_subnet_mask('0.255.255.192')
        self.assertFalse(result)

    def testConvertingBinaryStringToListHigh(self):
        result = utils.convert_binary_string_to_list(bin(255))
        for bit in result:
            self.assertEquals(bit, '1')

    def testConvertingBinaryStringToListLow(self):
        result = utils.convert_binary_string_to_list(bin(0))
        for bit in result:
            self.assertEquals(bit, '0')
    
    def testConvertingBinaryStringToListMid(self):
        result = utils.convert_binary_string_to_list(bin(85))
        for bit_index in range(0, len(result)):
            if(bit_index % 2 == 0):
                self.assertEquals(result[bit_index], '1')
            else:
                self.assertEquals(result[bit_index], '0')

    def testConvertingBinaryListToDecimalHigh(self):
        result = utils.convert_binary_to_dec(bin(255))
        self.assertEquals(result, 255)
    
    def testConvertingBinaryListToDecimalLow(self):
        result = utils.convert_binary_to_dec(bin(0))
        self.assertEquals(result, 0)

    def testConvertingBinaryListToDecimalMid(self):
        result = utils.convert_binary_to_dec(bin(85))
        self.assertEquals(result, 85)
        
    def testActiveBitsToBinaryHigh(self):
        result = utils.to_binary_from_active_bits(8)
        self.assertEquals(result, bin(255))
    
    def testActiveBitsToBinaryLow(self):
        result = utils.to_binary_from_active_bits(0)
        self.assertEquals(result, '0b' + bin(0)[2:].zfill(8))

    def testActiveBitsToBinaryMid(self):
        result = utils.to_binary_from_active_bits(2)
        self.assertEquals(result, bin(192))

    def testActiveBitsHigh(self):
        result = utils.count_active_bits(bin(255))
        self.assertEquals(result, 8)
    
    def testActiveBitsLow(self):
        result = utils.count_active_bits(bin(0))
        self.assertEquals(result, 0)

    def testActiveBitsMid(self):
        result = utils.count_active_bits(bin(85))
        self.assertEquals(result, 4)

    def testFindMaxedOctetsBitFormHigh(self):
        result = utils.find_maxed_octets('24', True)
        self.assertEquals(result, 3)

    def testFindMaxedOctetsBitFormLow(self):
        result = utils.find_maxed_octets('1', True)
        self.assertEquals(result, 0)

    def testFindMaxedOctetsBitFormMid(self):
        result = utils.find_maxed_octets('16', True)
        self.assertEquals(result, 2)

    def testFindMaxedOctetsNumberFormHigh(self):
        result = utils.find_maxed_octets('255.255.255.192', False)
        self.assertEquals(result, 3)

    def testFindMaxedOctetsNumberFormLow(self):
        result = utils.find_maxed_octets('192.0.0.0', False)
        self.assertEquals(result, 0)

    def testFindMaxedOctetsNumberFormMid(self):
        result = utils.find_maxed_octets('255.255.192.0', False)
        self.assertEquals(result, 2)

    def testFindActiveBitsBitFormHigh(self):
        result = utils.find_active_bits('23', True)
        self.assertEquals(result, 7)

    def testFindActiveBitsBitFormLow(self):
        result = utils.find_active_bits('24', True)
        self.assertEquals(result, 0)

    def testFindActiveBitsBitFormMid(self):
        result = utils.find_active_bits('25', True)
        self.assertEquals(result, 1)

    def testFindActiveBitsNumberFormHigh(self):
        result = utils.find_active_bits('255.255.255.254', False)
        self.assertEquals(result, 7)

    def testFindActiveBitsNumberFormLow(self):
        result = utils.find_active_bits('255.255.255.0', False)
        self.assertEquals(result, 0)

    def testFindActiveBitsNumberFormMid(self):
        result = utils.find_active_bits('255.255.255.224', False)
        self.assertEquals(result, 3)
   
    

if __name__ == '__main__':
    unittest.main()