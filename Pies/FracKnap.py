# Uses python3
import sys

def get_optimal_value(capacity, weights, values): # get input capacity as integer; weights and values as lists of same size
    
    value = 0. # initialize value to be returned as float

    unit_vals = [] # list/vector to store calculated unit values
    sack = [] # list/vector to hold candidate items

    v_w = zip(values,weights) # create zip object linking values of items to corresponding weights

    for v,w in v_w: # iterate over pairs in zip object
        unit_vals.append(v/w) # calculate unit values of value weight pairs and append to unit value list

    n = len(values) # n is the number of items
        
    while (capacity > 0) and (n > 0): # while sack isn't full & items are remaining
        
        best_index = unit_vals.index(max(unit_vals)) # on each iteration get index of the item with highest unit value (best item)
        
        if weights[best_index] <= capacity: # check to see if weight of best item is less than or equal to remaining capacity
           sack.append(values[best_index]) # add item to sack
           capacity -= weights[best_index] # reduce capacity by weight of current best item
           unit_vals[best_index] = 0 # 'remove' this item from potential items for selection in next iteration
           n -= 1 # reduce number of items to be considered
           
        else: # if weight of best item is greater than capacity
            sack.append((values[best_index])*(capacity/weights[best_index])) # add to sack a proportional amount of the item
            capacity -= weights[best_index] # reduce capacity by weight of current best item
            unit_vals[best_index] = 0 # 'remove' this item from potential items for selection in next iteration
            n -= 1 # reduce number of items to be considered
            

    print(unit_vals)
    print(sack)
    print(capacity)
    value = sum(sack)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
