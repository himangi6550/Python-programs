#to print the fibonacci series till n
def fibonacci(a,b):
    c=a+b
    if c<n:
        print(c,end=" ")
        fibonacci(b,c)
         
a=0
b=1
n=int(input("Enter the value of n: "))
print("Fibonacci Series")
print(a,b,end=" ")
fibonacci(a,b)



#to print the nth term
num=int(input("\nenter the nth term: "))

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(num))


