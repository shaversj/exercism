result = []


def flatten(iterable):

    for char in iterable:
        if isinstance(char, list):
            flatten(char)
        elif char is None:
            pass
        else:
            result.append(char)

    return result

