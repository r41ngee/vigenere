def word_fill(key: str, word_size: int) -> str:
    if len(key) > word_size:
        return key[:word_size]
    elif len(key) == word_size:
        return key
    else:
        tempkey = key
        for i in range(len(key), word_size):
            tempkey += key[i % len(key)]

        return tempkey


if __name__ == "__main__":
    print(word_fill("lemon", len("lemon")))
