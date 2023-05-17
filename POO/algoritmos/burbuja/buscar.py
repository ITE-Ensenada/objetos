def Find(array, num):
    find = []
    for i in range(len(array)):
        if array[i] == num:
            find.append(i)
    return find

def Search(array, num):
    find=Find(array, num)
    if find:
        print(f"Tu numero se encontro en las posiciones {find}")
    else: print("Tu numero no esta, bye")
