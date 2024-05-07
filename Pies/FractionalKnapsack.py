# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    unit_vals = []
    sack = []
   
    v_w = zip(values,weights)

    for v,w in v_w:
        unit_vals.append(v/w)

    while (capacity != 0):

        sack.append(values[unit_vals.index(max(unit_vals))])
        capacity -= weights[unit_vals.index(max(unit_vals))]

    print(unit_vals)
    print(sack)
    print(capacity)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
