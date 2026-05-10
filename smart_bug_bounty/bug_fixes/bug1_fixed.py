def get_last_n(items, n):
    result = []
    start = len(items) - n
    for i in range(start, len(items)):
        result.append(items[i])
    return result