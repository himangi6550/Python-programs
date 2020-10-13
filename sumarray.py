N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = [N]

# Write the logic here:
for i in numArray1:
    sumArray[i]=i


# Print the sumArray
for element in sumArray:
    print(element, end=" ")

print("")
