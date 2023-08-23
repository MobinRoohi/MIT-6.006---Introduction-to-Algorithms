def move(list : list, i, k, j):
    if k < 1: 
        return
    x = list.pop(i)
    if j > i:
        list.insert(j - 1, x)
        move(list, i, k - 1, j)
    else:
        list.insert(j, x)
        move(list, i + 1, k - 1, j + 1)

lst = list(range(10))
move(lst, 7, 3, 1)
print(lst)
        
