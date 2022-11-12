def left_rotate(dword, bits):
    return ((dword << bits) | (dword >> (32 - bits))) & 0xFFFFFFFF


if __name__ == "__main__":
    cipher = "0A 00 00 00 0E 00 00 40 0D 00 00 E0 0C 00 00 60 0C 00 00 A0 0E 00 00 60 0E 00 00 60 09 00 00 00 0C 00 " \
             "00 20 0C 00 00 60 0D 00 00 60 0C 00 00 A0 0E 00 00 40 05 00 00 C0 0C 00 00 A0 0F 00 00 00 0C 00 00 A0 "
    cipher = cipher.replace(" ", "")
    for i in range(0, len(cipher), 8):
        cipher_char = ""

        # char stored in little endian
        for j in range(i, i + 8, 2):
            cipher_char = cipher[j:j + 2] + cipher_char

        # Convert to hex string to decimal
        hex_int = int(cipher_char, 16)

        # Do left rotate to reverse right rotate of 3
        rotated = left_rotate(hex_int, 3)

        # Print character
        print(chr(rotated), end="")
