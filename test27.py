import unittest
from unittest.mock import patch
from program27 import Hex_Mem_Stack_Calculator

class CalculatorTestCases(unittest.TestCase):
    """ Test suite for Hex Memory Stack Calculator methods."""
    def setUp(self):
        """ Create a calculator instance before every test"""
        self.calculator = Hex_Mem_Stack_Calculator()
        
    def _capture_output(self, mocked_print):
        """Helper to capture printed output."""
        printed = []
        def fake_print(*args, **kwargs):
            printed.append(' '.join(str(arg) for arg in args))
        mocked_print.side_effect = fake_print
        return printed
        
    @patch('builtins.input', side_effect = ['0', '1', '255', '256', '32767', '32768', '65535', '-1', '-32768', 'back'])
    @patch('builtins.print')
    def test_bin16(self, mocked_print, mocked_input):
        """ Decimal to binary converter test"""
        printed = self._capture_output(mocked_print)
        self.calculator.dec_hex_bin()
        binary_lines = [line for line in printed if "BIN(16) = <" in line] # Read the result
        self.assertEqual(len(binary_lines), 9) # Find the length of each test value
        for line in binary_lines:
            bin_str = line.split('<')[1].split('>')[0]
            self.assertEqual(len(bin_str), 16, f"Binary length is not 16: {bin_str}")
            
    @patch('builtins.input', side_effect=['32768', '65535', 'back'])
    @patch('builtins.print')
    def test_signed16(self, mocked_print, mocked_input):
        """ Decimal to binary converter test. Performs test on the signed16 output """
        printed = self._capture_output(mocked_print)
        self.calculator.dec_hex_bin()
        signed_lines = [line for line in printed if "SIGNED16 = <" in line]
        self.assertEqual(len(signed_lines), 2)
        self.assertIn("SIGNED16 = <-32768>", signed_lines[0])
        self.assertIn("SIGNED16 = <-1>", signed_lines[1])

    @patch('builtins.input', side_effect = ['0', '0x1000', 'back'])
    @patch('builtins.print')
    def test_little_endian_1(self, mocked_print, mocked_input):
        """Pack/unpack n=0 at address 0x1000."""
        printed = self._capture_output(mocked_print)
        self.calculator.little_endian()
        self.assertIn("LOW BYTE = <0>", printed)
        self.assertIn("HIGH BYTE = <0>", printed)
        self.assertIn("UNPACKED = <0>", printed)
        self.assertIn("MEM[0x1000] = 0x00", printed)
        self.assertIn("MEM[0x1001] = 0x00", printed)

    @patch('builtins.input', side_effect = ['1', '0x2000', 'back'])
    @patch('builtins.print')
    def test_little_endian_2(self, mocked_print, mocked_input):
        """Pack/unpack n=0 at address 0x2000."""
        printed = self._capture_output(mocked_print)
        self.calculator.little_endian()
        self.assertIn("LOW BYTE = <1>", printed)
        self.assertIn("HIGH BYTE = <0>", printed)
        self.assertIn("UNPACKED = <1>", printed)
        self.assertIn("MEM[0x2000] = 0x01", printed)
        self.assertIn("MEM[0x2001] = 0x00", printed)

        
    @patch('builtins.input', side_effect = ['255', '0x3000', 'back'])
    @patch('builtins.print')
    def test_little_endian_3(self, mocked_print, mocked_input):
        """Pack/unpack n=255 at address 0x3000."""
        printed = self._capture_output(mocked_print)
        self.calculator.little_endian()
        self.assertIn("LOW BYTE = <255>", printed)
        self.assertIn("HIGH BYTE = <0>", printed)
        self.assertIn("UNPACKED = <255>", printed)
        self.assertIn("MEM[0x3000] = 0xFF", printed)
        self.assertIn("MEM[0x3001] = 0x00", printed)

    @patch('builtins.input', side_effect = ['256', '0x4000', 'back'])
    @patch('builtins.print')
    def test_little_endian_4(self, mocked_print, mocked_input):
        """Pack/unpack n=256 at address 0x3000."""
        printed = self._capture_output(mocked_print)
        self.calculator.little_endian()
        self.assertIn("LOW BYTE = <0>", printed)
        self.assertIn("HIGH BYTE = <1>", printed)
        self.assertIn("UNPACKED = <256>", printed)
        self.assertIn("MEM[0x4000] = 0x00", printed)
        self.assertIn("MEM[0x4001] = 0x01", printed)
        
    @patch('builtins.input', side_effect = ['HELLO'])
    @patch('builtins.print')
    def test_ascii_dump_lines(self, mocked_print, mocked_input):
        """ ASCII dump test"""
        printed = self._capture_output(mocked_print)
        result = self.calculator.ascii_dump()
        expected = [
            (0x1000, ord('H')),
            (0x1001, ord('E')),
            (0x1002, ord('L')),
            (0x1003, ord('L')),
            (0x1004, ord('O')),
            (0x1005, 0x00)
        ]
        self.assertEqual(result, expected)
        self.assertIn("0x1000 : 0x48", printed)
        self.assertIn("0x1001 : 0x45", printed)
        self.assertIn("0x1002 : 0x4C", printed)
        self.assertIn("0x1003 : 0x4C", printed)
        self.assertIn("0x1004 : 0x4F", printed)
        self.assertIn("0x1005 : 0x00", printed)
        self.assertIn("LENGTH (until 0x00) = 5", printed)

    @patch('builtins.input', side_effect = ['yes', '1000', '3', '2', 'read', 'back'])
    @patch('builtins.print')
    def test_element_address(self, mocked_print, mocked_input):
        """Test array addressing example"""
        printed = self._capture_output(mocked_print)
        self.calculator.array_addressing()
        self.assertIn("ADDRESS = base + index*size = 0x3ee", printed)
        self.assertIn("READ size=2 from ADDRESS 0x3ee = 0", printed)
        
    @patch('builtins.input', side_effect = ['15 25', 'back'])
    @patch('builtins.print')
    def test_stack_frame_lines(self, mocked_print, mocked_input):
        """ Stack frame test"""
        printed = self._capture_output(mocked_print)
        self.calculator.stack_frame()
        self.assertIn("bp     : RETURN", printed)
        self.assertIn("bp+2   : a = 15", printed)
        self.assertIn("bp+4   : b = 25", printed)
        self.assertIn("AX = 15", printed)
        self.assertIn("BX = 25", printed)
        self.assertIn("AX (AX+BX) = 40", printed)

    @patch('builtins.input', side_effect=[
        'yes', '1000', '0', '1', 'write', '42',
        'yes', '1000', '0', '1', 'read',
        'back'
    ])
    @patch('builtins.print')
    def test_array_memory_write_read(self, mock_print, mock_input):
        """Write a byte then read it back using array addressing."""
        printed = self._capture_output(mock_print)
        self.calculator.array_addressing()
        self.assertIn("WRITE size=1 value=42 to ADDRESS 0x3e8", printed)  # 1000 in hex = 0x3e8
        self.assertIn("READ size=1 from ADDRESS 0x3e8 = 42", printed)

if __name__ == '__main__':
    unittest.main()
