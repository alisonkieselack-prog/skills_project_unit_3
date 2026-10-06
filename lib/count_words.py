def count_words(string):
    if type(string) == str:
        return len(string.split())
    else:
        raise AttributeError("Argument must be a string")