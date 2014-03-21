import math

def scalar(vector):
    return math.sqrt(sum(x * x for x in vector.values()))

def similarity(a, b):
    if a == {} or b == {}:
        return 0.0

    numer = sum(a[k] * b.get(k, 0) for k in a)
    return numer / (scalar(a) * scalar(b))

if __name__ == '__main__':
    d0 = {'vaio': 1, 'sony': 2, 'thinkpad': 3, 'apple': 4 }
    d1 = {'apple': 1, 'ipod': 2, 'thinkpad': 3, 'sony': 4 }
    print(similarity(d0, d1))
