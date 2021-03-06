"""CPU functionality."""

import sys

ram = [0] * 256
reg = [0] * 8
pc = 0

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR = ram[pc]
        operand_a = self.ram_read(pc + 1)
        operand_b = self.ram_read(pc + 2)
        #if IR == 'ADD':


    def ram_read(self, address):
        """
        MDR - data that was read or written to
        """
        return self.ram[address]

    def ram_write(self, value, address):
        """
        MAR address being read or written to
        """
        self.ram[address] = value

    def LDI(self):
        self.alu('ADD', reg_a, reg_b)
        pass

    def PRN(self, reg_number):
        print(self.reg[reg_number])

    def HLT(self):
        sys.exit()