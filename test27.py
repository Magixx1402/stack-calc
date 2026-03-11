#import pytest
import unittest

from unittest.mock import patch
from io import StringIO

from program27 import Hex_Mem_Stack_Calculator 

class TestHexMemStackCalculator(unittest.TestCase):

    def setUp(self):
        """Runs before every test to provide a fresh calculator instance."""
        self.calc = Hex_Mem_Stack_Calculator()

    @patch('builtins.input', side_effect=['255', 'back'])
    def test_dec_hex_bin_positive(self, mocked_input):
        """Tests decimal to hex/bin conversion."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calc.dec_hex_bin()
            output = fake_out.getvalue()
            
            self.assertIn("HEX = <FF>", output)
            self.assertIn("BIN(16) = <0000000011111111>", output)

    @patch('builtins.input', side_effect=['-1', 'back'])
    def test_dec_hex_bin_negative(self, mocked_input):
        """Tests negative number 16-bit handling."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calc.dec_hex_bin()
            output = fake_out.getvalue()
            
            # -1 in 16-bit unsigned hex is FFFF
            self.assertIn("HEX = <FFFF>", output)

    @patch('builtins.input', side_effect=['4660', '0x2000', 'back'])
    def test_little_endian(self, mocked_input):
        """Tests byte splitting and memory addressing."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calc.little_endian()
            output = fake_out.getvalue()
            
            # 4660 = 0x1234 -> Low: 0x34 (52), High: 0x12 (18)
            self.assertIn("LOW BYTE = <52>", output)
            self.assertIn("HIGH BYTE = <18>", output)
            self.assertIn("MEM[0x2000] = 0x34", output)

    @patch('builtins.input', return_value='Hello World')
    def test_ascii_dump_truncation(self, mocked_input):
        """Tests that strings are capped at 10 characters."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calc.ascii_dump(base_address=0x1000)
            output = fake_out.getvalue()
            
            # 'Hello Worl' is 10 chars. The 11th byte (offset 10) must be 0x00
            self.assertIn("0x100a : 0x00", output)
            self.assertIn("LENGTH (until 0x00) = 10", output)

    @patch('builtins.input', side_effect=['10 20', 'back'])
    def test_stack_frame(self, mocked_input):
        """Tests BP offset simulation and AX/BX addition."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calc.stack_frame()
            output = fake_out.getvalue()
            
            self.assertIn("bp+2   : a = 10", output)
            self.assertIn("bp+4   : b = 20", output)
            self.assertIn("AX (AX+BX) = 30", output)

if __name__ == '__main__':
    unittest.main()