#inputs
nums = list(map(int,input().split()))
k = int(input())

#rotation
k %= len(nums)
l = len(nums)
nums[:] = nums[l-k:] + nums[:l-k]
print(nums)