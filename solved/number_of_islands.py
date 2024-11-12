class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_of_island = 0

        def dfs(i,j):
            if i<0 or i>= m or j>=n or j<0 or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i-1,j)
                dfs(i+1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_of_island +=1
                    dfs(i,j)

        return num_of_island