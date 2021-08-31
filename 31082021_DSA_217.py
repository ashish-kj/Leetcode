#input
nums = list(map(int, input().split()))

#process

final_set = set(nums)
if(len(final_set)==len(nums)):
    print(False)
else:
    print(True)