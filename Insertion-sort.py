#Write a program that sorts an array using the insertion-sort algorithm. 

arr=[15,30,22,25]

n = len(arr) 

for i in range(1, n): 
    key = arr[i] 
    j = i-1
    while j >= 0 and key < arr[j]:  
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key 

print(arr)