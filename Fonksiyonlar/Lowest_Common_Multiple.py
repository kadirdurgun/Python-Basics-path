def lowest_cm(num1,num2):
    i = 2
    lcm = 1
    while True:
        if (num1 % i == 0 and num2 % i == 0):
            lcm *= i

            num1 //= i
            num2 //= i
        elif (num1 % i != 0 and num2 % i ==0):
            lcm *= i

            num2 //= i
        elif(num1 % i == 0 and num2 % i !=0):
            lcm *= i

            num1 //= i
        else:
            i += 1
        if ( num1 == 1 and num2 == 1):
            break
    return lcm
num1=int(input("1st Number  : "))
num2=int(input("2nd Number : "))
print("The lowest common multiple of numbers is : ",lowest_cm(num1,num2))