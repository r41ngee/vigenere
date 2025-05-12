def word_fill(key: str, word_size: int) -> str:
    key_size = len(key)

    if key_size > word_size:
        return key[:word_size]
    elif key_size == word_size:
        return key
    else:
        tempkey = key
        for i in range(key_size, word_size):
            tempkey += key[i % key_size]

        return tempkey
