
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
        'and'   : '1001 R D',
        'outi'  : '1110 X D'
    }
}
