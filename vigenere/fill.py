def word_fill(key: str, word_size: int) -> str:
    if len(key) > word_size:
        return key[:word_size]
    elif len(key) == word_size:
        return key
