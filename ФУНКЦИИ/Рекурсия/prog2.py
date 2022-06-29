def recursive_reverse(lst):
    new_lst = []
    if not lst:
        return []
    new_lst.extend([lst[-1]] + recursive_reverse(lst[:-1]))
    return new_lst


print(recursive_reverse([1, 2, 3, "go go go"]))