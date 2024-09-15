def apply_all_func(int_list, *functions):
    results = {}
    int_list = list(map(int, int_list))
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func(['6', '20', '15', '9'], len, sum, sorted))
