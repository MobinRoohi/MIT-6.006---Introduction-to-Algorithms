def count_long_subarray(A):
    ls = list()
    max = 1
    for i in range(len(A)):
        curr = A[i]
        listed = [curr]
        for j in range(i + 1, len(A)):
            if A[j] <= curr:
                break
            curr = A[j]
            listed.append(A[j])
        if len(listed) == max:
            ls.append(listed)
        elif len(listed) > max:
            ls = [listed]
            max = len(listed)
    return len(ls)

if __name__ == '__main__':
    tpl = [int(item) for item in input().split(", ")]
    print(count_long_subarray(tpl))