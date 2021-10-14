#input the array
heights = list(map(int, input().split()))

#copy of the original array
sorted_heights = [0]*(len(heights))
for i in range(len(heights)):
    sorted_heights[i] = heights[i]

#sorting the array
sorted_heights.sort()

#counter for invalid spaces
counter = 0

#looping

for i in range(len(heights)):
    if heights[i] != sorted_heights[i]:
        counter+=1
print(counter)