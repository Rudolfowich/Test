my_list = [2, 6, 7, 9, 14, 22, 66, 221]
lesser = 4
result = []


def slice_less():
    for item in my_list:
        if item > lesser:
            result.append(item)
            result.sort(reverse=True)
    return result


print(slice_less())
