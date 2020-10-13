n=int(input("Enter a no."))
num=int(input("Enter either 0 or 1: "))
b=bool(num)

if b== True:
    for i in range(1,n+1):
        print(i*"*")
        
elif b== False:
    for i in range(n,0,-1):
        print(i*"*")
        

