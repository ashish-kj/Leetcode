#input grid
m = int(input())
n = int(input())

grid = []

for i in range(m):
    temp = []
    for j in range(n):
        temp.append(int(input()))
    grid.append(temp)

def numIslands(grid):
        islandCount = 0
        
        def creep(i, j, matrix):
            # if already explored, then return
            if matrix[i][j] == "0" or matrix[i][j] == "x" :
                return 
            # mark 1 to x so it wont interfere again
            if matrix[i][j] == "1":
                matrix[i][j] = "x"
            
            if i < len(matrix) - 1:
                creep(i + 1, j, matrix)
            if j < len(matrix[0]) - 1:
                creep(i, j + 1, matrix)
            if i > 0:
                creep(i - 1, j, matrix)
            if j > 0:
                creep(i, j - 1, matrix)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount += 1
                    creep(i, j, grid)
        
        print(islandCount)
print(grid)
print("=====================")
numIslands(grid)