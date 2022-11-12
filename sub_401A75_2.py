import base64

if __name__ == "__main__":
    encoded_strs = [
        "VnWoDLiwE3KNgkRuWXOqZL+lATOmF7V=", "VacwZLKwCjOmF7V=", "VacwZLKwCkZJenWNAR==", "Sn+tA7WzRLiiCnEmDKAqAYDvAYim",
        "ZY2qCX+vBYSwDjKNh4ZvAYim", "ZY2qYLywALEmDjOmF7V=", "A7mzEL6JZLiGEXlvAYim "
    ]

    custom_b64 = "1234567abcdefghQRSTUVWXYZABCDEFGHijklmnopqrstuvwxyzIJKLMNOP89+/0"
    std_b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    for encoded in encoded_strs:
        encoded = encoded.translate(str.maketrans(custom_b64, std_b64))
        flag = base64.b64decode(encoded)
        print(flag.decode())
