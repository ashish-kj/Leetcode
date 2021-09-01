#input the array
nums = list(map(int, input().split()))

#squaring
for i in range(len(nums)):
    nums[i] = nums[i]**2

#sorting
nums.sort()

#return
print(nums)