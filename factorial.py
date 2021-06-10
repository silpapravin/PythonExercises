def factorial(num):
    product=1
    while(num != 0):
        product=product*num
        num=num-1
    print("Factorial is : ",product)
    return

num=int(input("enter a number"))
factorial(num)