def slices(series, length):
    begin = 0
    end = length
    final_list = []

    if length <= 0:
        raise ValueError("Length is less than or equal to 0")
    if length > len(series):
        raise ValueError("Length is larger than series")

    for _ in series:
        value = series[begin:end]
        if len(value) == length:
            final_list.append(value)
            begin += 1
            end += 1

    return final_list
