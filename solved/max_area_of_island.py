class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        max_area = 0
        current_land_area = [0]
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j>=n or j<0 or grid[i][j] != 1:
                return
            else:
                current_land_area[0] +=1
                grid[i][j] = 0
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)
                dfs(i+1,j)
        

        for i in range(m):
            for j in range(n):
                print("current land ",current_land_area[0])
                if grid[i][j] == 1:
                    current_land_area = [0]
                    dfs(i,j)
                    
                    max_area = max(max_area,current_land_area[0])
                
        
        return max_area
                

s = Solution()
print(s.maxAreaOfIsland(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))