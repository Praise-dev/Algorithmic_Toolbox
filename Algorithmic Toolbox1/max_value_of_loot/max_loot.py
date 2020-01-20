# Uses python3
import sys

def get_unit_values(W, V):
    n = len(W)
    unit_values =[]
    for i in range(n):
            if W[i] > 0:
                unit_values.append(V[i] // W[i])
            else:
                unit_values.append(0)
    return unit_values


def get_optimal_value(capacity, weights, values):
    total_value = 0
    unit_values = get_unit_values(weights, values)
    weight = {}
    value = {}
    cap = capacity
    for unit_val in unit_values:
        weight[unit_val] = weights[unit_values.index(unit_val)]
        value[unit_val] = values[unit_values.index(unit_val)]

    while cap > 0 and unit_values:
        max_value = max(unit_values)
        if cap - weight.get(max_value) >= 0:
            total_value += value.get(max_value)
            cap -= weight.get(max_value)
        else:
            fraction = cap / weight.get(max_value)
            total_value += (value.get(max_value) * fraction)
            cap -= weight.get(max_value) * fraction
        unit_values.remove(max_value)

    return round(total_value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
