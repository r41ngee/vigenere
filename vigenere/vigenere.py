from fill import word_fill

ALPHABET = [chr(i).lower() for i in range(97, 123)]


def encrypt(word: str, key: str) -> str:
    word = word.lower()
    key = key.lower()

    if len(word) > len(key):
        key = word_fill(key, word)

    result = ""

    for i in range(len(word)):
        if word[i] not in ALPHABET:  # Пропускаем не-буквы
            result += word[i]
            continue

        key_char = key[i]
        word_char = word[i]

        new_index = (ALPHABET.index(word_char) + ALPHABET.index(key_char)) % 26
        result += ALPHABET[new_index]

    return result


def decrypt(crypted: str, key: str) -> str:
    key = key.lower()
    crypted = crypted.lower()

    if len(crypted) > len(key):
        key = word_fill(key, crypted)

    result = ""

    for i in range(len(crypted)):
        if crypted[i] not in ALPHABET:
            result += crypted[i]
            continue

        new_char = ALPHABET[ALPHABET.index(crypted[i]) - ALPHABET.index(key[i]) % 26]
        result += new_char

    return result
