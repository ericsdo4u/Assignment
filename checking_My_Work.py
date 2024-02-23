def get_String(words):
    result = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            result.append(word)
        return result