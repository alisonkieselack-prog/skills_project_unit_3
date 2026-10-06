def count_words(string):
    if type(string) == str:
        x = string.replace(",", " ")
        return len(x.split())
    else:
        raise AttributeError("Argument must be a string")