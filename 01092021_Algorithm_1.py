#input 
nums = list(map(int, input().split()))
target = int(input())

#vars
ret = list()
temp = 0
l = len(nums)

#Algo

for i in range(l):
    for j in range(i+1,l):
        temp = nums[i] + nums[j]
        if(temp == target):
            ret.append(i)
            ret.append(j)
            break
print(ret)