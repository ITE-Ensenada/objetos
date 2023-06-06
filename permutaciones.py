def permutaciones(arr):
    if len(arr) == 0:
        return [[]]

    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutaciones(rest):
            result.append([arr[i]] + p)

    return result