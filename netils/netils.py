import struct

def build_byte_string(hex_stream):
    """Converts a hex string (e.g. "928a83") into a byte string
    e.g. b"\x92\x8a\x83"
    """
    values = [int(x, 16) for x in map(''.join, zip(*[iter(hex_stream)]*2))]
    return struct.pack("!" + "B" * len(values), *values)
