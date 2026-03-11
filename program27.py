class Hex_Mem_Stack_Calculator:
    """ A class developed according to the system requirements"""
    def __init__(self):
        pass

    def dec_hex_bin(self):
        """ Converts a decimal number to 16-bit binary, 
        and its signed interpretation"""
        
        print("===== Decimal Converter ===== ")
        
        while True:
            num = input("Enter a decimal number or 'back' to return to main menu:- ")
            
            if num.lower() == 'back':
                print("Returning to main menu...")
                break
            
            try:
                n = int(num)
                
                # Check if number provided is less than 0 (necessary for negative number conversion)
                if n < 0:
                    # Add 65536 to get the unsigned equivalent
                    unsigned_n = n + 65536 # Unsigned integer representing non-negative numbers
                else:
                    unsigned_n = n

                hexadecimal_value = format(unsigned_n, 'X') # Convert to hexadecimal with hex function
                binary_value = format(unsigned_n, '016b') # Convert to binary with leading zeros
                
                if unsigned_n < 32768:
                    signed_value = unsigned_n
                else:
                    signed_value = unsigned_n - 65536
        
                print(f"HEX = <{hexadecimal_value}>")
                print(f"BIN(16) = <{binary_value}>")
                print(f"SIGNED16 = <{signed_value}>")

            # If input is a string
            except ValueError:
                print("Error: Please enter a valid integer (numbers only, no letters or symbols)")
      
    def little_endian(self):
        """Little-endian pack/unpack (16-bit) with memory write/read"""

        print("===== Little-Endian Pack/Unpack (16-bit) =====")

        # Simulated memory as dictionary
        memory = {}

        while True:
            num_input = input("Enter integer n (0–65535) or 'back' to return:- ")

            if num_input.lower() == 'back':
                print("Returning to main menu...")
                break

            try:
                n = int(num_input)

                if n < 0 or n > 65535:
                    print("Error: n must be between 0 and 65535.")
                    continue

                addr_input = input("Enter memory address (decimal or hex e.g. 0x2000):- ")

                # Accept decimal or hex
                if addr_input.lower().startswith("0x"):
                    addr = int(addr_input, 16)
                else:
                    addr = int(addr_input)

                # Extract bytes
                low_byte = n & 0xFF
                high_byte = (n >> 8) & 0xFF

                # Pack into memory (little-endian)
                memory[addr] = low_byte
                memory[addr + 1] = high_byte

                # Read back
                read_low = memory[addr]
                read_high = memory[addr + 1]

                # Unpack
                unpacked = read_low + (read_high << 8)

                # Required outputs
                print(f"LOW BYTE = <{low_byte}>")
                print(f"HIGH BYTE = <{high_byte}>")
                print(f"UNPACKED = <{unpacked}>")

                # Memory write evidence
                print(f"MEM[0x{addr:04X}] = 0x{low_byte:02X}")
                print(f"MEM[0x{addr+1:04X}] = 0x{high_byte:02X}")

                # Memory read evidence
                print(f"READ MEM[0x{addr:04X}] = 0x{read_low:02X}")
                print(f"READ MEM[0x{addr+1:04X}] = 0x{read_high:02X}")

            except ValueError:
                print("Error: Please enter valid numeric values.")

    def ascii_dump(self, base_address: int = 0x1000):
        """Array addressing using offsets (base + index × element size)"""
        user_input = input("Enter a string (maximum 10 characters): ")
    
        # 1. Logic: Constrain string length to 10 characters
        truncated_string = user_input[:10]
    
        # 2. Logic: Convert to ASCII values and append null terminator (0x00)
        byte_values = [ord(char) for char in truncated_string] + [0x00]
    
        # 3. UI: Format and print each byte with its memory address
        for i, val in enumerate(byte_values):
            current_address = base_address + i
            print(f"0x{current_address:04x} : 0x{val:02X}")
    
        # 4. UI: Print the length excluding the null terminator
        print(f"LENGTH (until 0x00) = {len(truncated_string)}")
    
    def array_addressing(self):
        """To be implemented"""
        pass
  
    def stack_frame(self):
        """Simplified bp offsets and register-style simulation"""
        print("\n===== Stack Frame (bp offsets) =====")
        
        while True:
            user_input = input("Enter two integers a and b (separated by space) or 'back':- ")
            
            if user_input.lower() == 'back':
                print("Returning to main menu...")
                break
            
            try:
                # Split input into two parts and convert to integers
                parts = user_input.split()
                if len(parts) != 2:
                    print("Error: Please enter exactly two integers.")
                    continue
                
                a = int(parts[0])
                b = int(parts[1])
                
                # 1. Stack Table View
                print("\n--- Stack Table ---")
                print(f"bp     : RETURN")
                print(f"bp+2   : a = {a}")
                print(f"bp+4   : b = {b}")
                
                # 2. Register-Style View
                print("\n--- Register View ---")
                print(f"AX = {a}")
                print(f"BX = {b}")
                # Simulating the addition operation within the AX register
                print(f"AX (AX+BX) = {a + b}")
                print("-" * 20 + "\n")

            except ValueError:
                print("Error: Please enter valid integers (e.g., 10 20).")
  
def main():
    """ An interactive menu for the program """
    calculator = Hex_Mem_Stack_Calculator()
    
    # Using strings as keys to match input()
    actions = {
            "1": calculator.dec_hex_bin,
            "2": calculator.little_endian,
            "3": calculator.ascii_dump,
            "4": calculator.array_addressing,
            "5": calculator.stack_frame,  # Fixed: Removed () - now references method
            "0": "exit"  # Special marker for exit
        }
    
    print("==============================")
    print(" Hex Memory & Stack Calculator")
    print("==============================")
    print("1. Convert (decimal -> hex and 16-bit binary)")
    print("2. Little-endian pack/unpack (16-bit)")
    print("3. ASCII Memory Dump")
    print("4. Array Addressing")  
    print("5. Stack frame (bp offsets)")
    print("0. Exit")
    
    while True:
            choice = input("\nEnter your choice:- ")
            
            if choice in actions:
                if choice == "0":
                    print("Thank you for using the program")
                    break
                else:
                    # All options now handle their own input and looping
                    actions[choice]()  # Call the method (no calculator argument needed)
            else:
                print("Invalid choice. Please enter a number between 0-5.")

if __name__ == "__main__":
    main()