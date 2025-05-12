def word_fill(key: str, word_size: int) -> str:
    key = (key * ((word_size // len(key)) + 1))[:word_size]
