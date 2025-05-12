from fill import word_fill

ALPHABET = [chr(i).lower() for i in range(97, 123)]


def cypher(word: str, key: str) -> str:
    word = word.lower()
    key = key.lower()

    if len(word) > len(key):
        key = word_fill(key, word)

    result = ""

    for i in range(len(word)):
        key_lit = key[i]
        word_lit = word[i]

        result += ALPHABET[(ALPHABET.index(key_lit) + ALPHABET.index(word_lit)) % 25]

    return result


if __name__ == "__main__":
    print(cypher("ATTACKATDAWN", "LEMON"))
