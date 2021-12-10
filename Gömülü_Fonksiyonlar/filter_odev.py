
def traingle(tupple):
    if (abs(tupple[0]+tupple[1]) > tupple[2] and abs(tupple[1]+tupple[2]) > tupple[0] and abs(tupple[0]+tupple[2]) > tupple [1]):
        return True
    else:
        return False

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(traingle,liste)))

