def combinaciones(arr, r):
    if r == 0:
        return [[]]

    if r > len(arr):
        return []

    result = []
    for i in range(len(arr)):
        rest = arr[i+1:]
        for c in combinaciones(rest, r-1):
            result.append([arr[i]] + c)

    return result