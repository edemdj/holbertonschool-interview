#!/usr/bin/python3
" Module to validate UTF-8 encoding of a list of integers"
def validUTF8(data):
    " Function to validate if a list of integers represents valid UTF-8 encoding"
    num_bytes = 0

    for byte in data:
        # We only care about the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count leading 1's to determine byte length
            if byte >> 7 == 0:
                continue  # 1-byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Continuation byte must start with 10
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
