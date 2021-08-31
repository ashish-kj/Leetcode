#input array
arr = list(map(int, input().split()))

#init vars
sumo = 0
best = 0

#logic code
for i in range(len(arr)):
    
    if sumo+arr[i]<arr[i]:
        sumo = arr[i]
    else: 
        sumo += arr[i]
    
    if sumo > best:
        best = sumo
    
        
print(best)

