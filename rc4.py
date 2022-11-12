if __name__ == "__main__":
    S = []
    key = "Ul0v3M@lwArE"
    key_length = len(key)
    j = 0
    for ch in range(256):
        S.append(ch)
    for ch in range(256):
        j = (S[ch] + j + ord(key[ch % key_length])) % 256
        S[ch], S[j] = S[j], S[ch]

    # Port and IP to decrypt
    ciphers = [[81, 215, 5, 47, 41], [83, 221, 3, 53, 44, 149, 75, 206, 201, 253, 37, 172, 108, 176]]

    S_bak = S.copy()

    for cipher in ciphers:
        i = 0
        j = 0
        K = []
        S = S_bak.copy()
        for ch in range(len(cipher)):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K.append(cipher[ch] ^ S[(S[i] + S[j]) % 256])
        for ch in range(len(K)):
            print(chr(K[ch]), end="")
        print()
