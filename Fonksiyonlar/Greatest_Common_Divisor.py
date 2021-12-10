def greatestcd(num1,num2):
    num1_divisors=list()
    num2_divisors=list()
    temp_divisor=0
    for i in range(1,num1+1):
        if(num1 % i == 0):
            num1_divisors.append(i)
    for j in range(1,num2+1):
        if(num2 % j == 0):
            num2_divisors.append(j)

    for k in num1_divisors:
        for m in num2_divisors:
            if(k == m):
                temp_divisor=k
    print("Number-1 Divisor List: ", num1_divisors)
    print("Number-2 Divisor List:", num2_divisors)

    return temp_divisor
num1 = int(input("Number - 1  : "))
num2 = int(input("Number - 2 :"))

print("\nGreatest Common Divisor of Numbers is : ",greatestcd(num1,num2))


