#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
EITF65 Assembler.

An assembler for the CPU lab in the course Digital Circuits at LTH.
Write the program in assembly with mnemonics and use this program
to translate it into machine code.

Project website: https://github.com/Noxet/eitf65_assembler

Jonathan Sönnerup
2017
"""

import sys

import isa

ILEN = isa.ISA['ilen']
RLEN = isa.ISA['rlen']
DLEN = isa.ISA['dlen']

def decode(instr: str) -> str:
    """Decodes an instruction and returns the coresponding machine code."""

    opcode, arg1, arg2 = instr[0].lower(), 0, 0
    if opcode not in isa.ISA['opcodes']:
        print('Opcode mnemonic [{}] not defined'.format(opcode))
        sys.exit(1)

    if len(instr) == 2:
        arg1 = int(instr[1])                # get data value
    elif len(instr) == 3:
        reg_x = instr[1].lower()
        arg1 = int(reg_x.split('r')[-1])    # get register value
        arg2 = int(instr[2])                # get data value

    # get the bit value of opcode menmonic
    opcode_bit = int(isa.ISA['opcodes'][opcode].split()[0], 2)

    # generate the corresponding machine code
    mcode = '{3:0{0}b}{5:0{1}b}{4:0{2}b}'       # only data
    if 'R' in isa.ISA['opcodes'][opcode]:
        mcode = '{3:0{0}b}{4:0{1}b}{5:0{2}b}'   # register with/without data

    return mcode.format(ILEN, RLEN, DLEN, opcode_bit, arg1, arg2)

def main(infile):
    """Opens the specified .s file and decodes it."""
    with open(infile, 'r') as f:
        instructions = f.read().strip().splitlines()

    mcodes = [decode(instr.split()) for instr in instructions]

    with open('{}.coe'.format(infile), 'w') as f:
        f.write('memory_initialization_radix=2;\n')
        f.write('memory_initialization_vector=\n')
        f.write('\n'.join(m for m in mcodes))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input file>' % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
