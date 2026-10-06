
def make_snippet(string):
    string_list = string.split(" ")
    if len(string_list) > 5:
        new_string = " ".join(string_list[0:5])
        return new_string + "..."
    return string