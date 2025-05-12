def word_fill(key: str, word: str) -> str:
    key = (key * ((len(word) // len(key)) + 1))[: len(word)]

    return key
