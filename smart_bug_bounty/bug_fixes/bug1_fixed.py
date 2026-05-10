def get_last_n(items, n):
    result = []
    start = len(items) - n
    # IndexError-un qarşısını almaq üçün range sonu düzəldildi
    for i in range(start, len(items)):
        result.append(items[i])
    return result