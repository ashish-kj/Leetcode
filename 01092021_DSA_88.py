#inputs
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
n = int(input())

#algo
nums1[:] = nums1[0:m] + nums2[:]
nums1.sort()
print(nums1)