#Uses python3

import sys

def max_dot_product(a, b):

    a.sort()
    b.sort()
    
    res = 0
    
    while len(a) > 0:
        res += a[-1] * b[-1]
        a.pop()
        b.pop()
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
