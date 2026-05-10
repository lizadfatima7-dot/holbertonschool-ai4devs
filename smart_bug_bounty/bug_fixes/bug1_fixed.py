def get_last_n(items, n):
    result = []
    start = len(items) - n
    # IndexError-un qarşısını almaq üçün + 1 silindi
    for i in range(start, len(items)):
        result.append(items[i])
    return result

my_list = [10, 20, 30, 40, 50]
print(get_last_n(my_list, 3))