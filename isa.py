
"""
EITF65 Assembler ISA.

Definition of the Instruction Set Architecture.
To add an instruction, simply add the opcode mnemonic in the
'opcodes' map. Specify whether the instruction uses register and/or immediate data
with R and D, respectively. If an instruction does not use a register or data, simply
write X instead.

Example:
The 'add' instruction specifies both a register and immediate data, thus should be encoded as
'iiii R D'
where 'iiii' is the opcode bitstring.

The 'bz' instruction does not specify immediate data, thus should be encoded as
'iiii R X'

Jonathan Sönneurp
2017
"""

ISA = {
    'ilen': 4,
    'rlen': 1,
    'dlen': 8,
    'opcodes': {
        'call'  : '0000 X D',
        'ret'   : '0001 X X',
        'bz'    : '0010 R X',
        'b'     : '0011 X D',
        'add'   : '0100 R D',
        'sub'   : '0101 R D',
        'ld'    : '0110 R D',
        'in'    : '0111 R X',
        'out'   : '1000 R X',
        'and'   : '1001 R D'
    }
}
