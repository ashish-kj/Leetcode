#initialise array and key value
nums = list(map(int, input().split()))
target = int(input())

#binary search algo

f = 0
l = len(nums) - 1

while(f<=l):
    m = (f+l)//2
    if(nums[m] == target):
        print(m)
        break
    else:
        if(nums[m]<target):
            f = m+1
        else:
            l = m-1
if(f>l):
    print("-1")
