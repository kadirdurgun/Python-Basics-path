def pisagor_list(num1,num2):
    list_of_pisagor = list()
    for i in range(1, num1):
        for j in range(1, num2):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                list_of_pisagor.append((i, j, int(c)))

    return print(list_of_pisagor)
num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number :"))
print("Possible pisagor triangle list is below :")
pisagor_list(num1,num2)
