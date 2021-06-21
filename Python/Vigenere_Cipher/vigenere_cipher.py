# Maps number to alphabets
alphabets_character_i_a = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z",
}

# Maps alphabet to number
alphabets_character_a_i = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

# Initialising Vigenere Cipher Table
vigenere_cipher_table = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

# Generating Vigenere Cipher Table
for i in range(0, 26):
    for j in range(0, 26):
        ind = (i + j) % 26
        vigenere_cipher_table[i].append(alphabets_character_i_a[ind + 1])

# Encoding Text according to Vigenere Cipher


def vigenere_cipher_enc(text, key):
    enc_text = ""
    den = len(key)
    for i in range(0, len(text)):
        enc_text = (
            enc_text
            + vigenere_cipher_table[alphabets_character_a_i[text[i].upper()] - 1][
                alphabets_character_a_i[key[i % den].upper()] - 1
            ]
        )
    return enc_text


# Decoding Text according to Vigenere Cipher


def vigenere_cipher_dec(key, enc):
    dec_text = ""
    den = len(key)
    for i in range(0, len(enc)):
        col = alphabets_character_a_i[key[i % den].upper()] - 1
        j = 0
        while vigenere_cipher_table[j][col] != enc[i].upper():
            j = j + 1
        dec_text = dec_text + alphabets_character_i_a[j + 1]
    return dec_text


if __name__ == "__main__":
    typ = input(
        "Do You want to encode or decode? Type 'e' for encryption and 'd' for decryption\n"
    )
    if typ == "e":
        text = input("Please enter the text you want to encode\n")
        key = input("Please enter the key\n")
        print("Encrypted Text: " + vigenere_cipher_enc(text, key))
    elif typ == "d":
        key = input("Please enter the key\n")
        enc = input("Please enter the text you want to decode\n")
        print("Decrypted Text: " + vigenere_cipher_dec(key, enc))
    else:
        print("Sorry you have enter the wrong input. Please try again\n")
