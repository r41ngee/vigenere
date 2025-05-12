def word_fill(key: str, word: int) -> str:
    key = (key * ((len(word) // len(key)) + 1))[: len(word)]
