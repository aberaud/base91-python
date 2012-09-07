import struct

basE91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
	'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
	'%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
	'>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']

decode_table = dict((v,k) for k,v in enumerate(basE91_alphabet))

def base91_decode(encoded_str):
    v = -1
    b = 0
    n = 0
    out = bytearray()
    for strletter in encoded_str:
        if not strletter in dectable:
            continue
        c = dectable[strletter]
        if(v < 0):
            v = c
        else:
            v += c*91
            b |= v << n
            n += 13 if (v & 8191)>88 else 14
            while True:
                out += struct.pack('B', b&255)
                b >>= 8
                n -= 8
                if not n>7:
                    break
            v = -1
    if v+1:
        out += struct.pack('B', (b | v << n) & 255 )
    return out
    
