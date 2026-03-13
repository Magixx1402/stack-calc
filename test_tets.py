import unittest
from unittest.mock import patch
from program27 import Hex_Mem_Stack_Calculator

# Draft test case, yet to be implemented
# The function naming corresponding with assessment requirements
class CalculatorTestCases(unittest.TestCase):
    """ Test suite for Hex Memory Stack Calculator methods."""
    
    def setup(self):
        """ Create a calculator instance before every test"""
        self.calculator = Hex_Mem_Stack_Calculator()
        
    @patch
    def bin16_test():
        """ Decimal to hexadecimal & binary test"""
        pass
    
    @patch
    def signed16_test():
        """ """
        pass
    
    @patch
    def little_endian_test_1():
        pass
    
    @patch
    def little_endian_test_2():
        pass
    
    @patch
    def little_endian_test_3():
        pass
    
    @patch
    def little_endian_test_4():
        pass
    
    @patch
    def ascii_dump_lines():
        """ ASCII dump test"""
        pass
    
    @patch
    def element_address():
        """ Array addressing test"""
        pass
    
    @patch
    def stack_frame_lines():
        """ Stack frame test"""
        pass
    
    @patch
    def memory_write():
        pass
