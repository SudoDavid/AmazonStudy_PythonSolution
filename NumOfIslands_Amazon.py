#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
class Solution(object):
  def numIslands(self, grid):
    if not grid:
        return 0
        
    m = len(grid)
    n = len(grid[0])
    sum  = 0
    
    for i in range(m):
        for j in range(n):
            
            if grid[i][j] == "0":
                continue
            else:
                
                #sum up only once per chance of meeting "1"
                sum += 1
                stack = list()
                stack.append([i,j])
                
                #visit each "1" in the adjacent area using a stack
                while len(stack) != 0:
                    
                    [p,q] = stack.pop()
                    
                    if p >= 1 and grid[p-1][q] == "1":
                        stack.append([p-1,q])
                        
                    if p < m -1 and grid[p+1][q] == "1":
                        stack.append([p+1,q])
                    
                    if q >= 1 and grid[p][q-1] == "1":
                        stack.append([p,q-1])
                        
                    if q < n - 1 and grid[p][q + 1] == "1":
                        stack.append([p,q+1])
                    
                    #mark as visited
                    grid[p][q] = "0"
    
    return sum