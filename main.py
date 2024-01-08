def depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(depth(item) for item in lst)


print(depth([1, [2, [3, [4, [5]]]]])) # 5