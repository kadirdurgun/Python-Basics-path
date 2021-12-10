from functools import reduce

def even_numbers(x):
    if (x % 2 == 0):
        return True
    else:
        return False
def add(i,j):
    return i+j


liste = [0,1,2,3,4,5,6,7,8,9,10]

listeeven = list(filter(even_numbers,liste))
print(reduce(add,listeeven))