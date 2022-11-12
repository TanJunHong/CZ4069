if __name__ == "__main__":
    b = bytearray(open("shellcode.bin", 'rb').read())
    for i in range(0x144, len(b)):
        b[i] ^= 0x66
    open("decoded.bin", "wb").write(b)
