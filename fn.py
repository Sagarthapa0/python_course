#Q. give a factorial of a given number.

def factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    print("factorial is",result)
    
a=int(input("enter a number "))
factorial(a)

# Q. series of a given number

def series(num):
    result=0
    for i in range(1,num+1):
        result +=i
    print(result)

num=int(input("enter num" ))
series(num)