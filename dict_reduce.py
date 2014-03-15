def dict_reduce(func, dicts, init_value, missing_value):
    keys = set()
    for d in dicts:
        keys |= d.keys()

    out = dict((k, init_value) for k in keys)
    for d in dicts:
        out = dict((k, func(v, d.get(k, missing_value))) for k, v in out.items())

    return out

if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 1, 'c': 2, 'd': 3}
    d3 = {'c': 1, 'd': 2, 'e': 3}
    merged = dict_reduce(lambda v1,v2: v1+v2, [d1, d2, d3], 0, 0)
    print(merged)
