def perfect_number(number):
    sum=0
    for i in range(1,number):
        if(number % i == 0):
            sum+=i
    return sum==number
for i in range (1,1000):
    if(perfect_number(i)):
        print(i," is Perfect number ..." )