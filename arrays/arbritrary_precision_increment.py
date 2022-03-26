"""
Arbritraty Precision Increment 

Given an array non-negative digits that represent a decimal interger 

add one to the integer. Assume the solution still works even if implemented in a laguage with finite precision arithmetic
"""


def precision_increment(arr):
    arr[-1] += 1 
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1
    
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


if __name__ == "__main__":
    
    print(precision_increment([9,9,9]))