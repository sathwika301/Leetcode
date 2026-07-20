class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        
        for c in range(k):
            mat=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==m-1 and j==n-1:
                        mat[0][0]=grid[m-1][n-1]
                    elif j<n-1:
                        mat[i][j+1]=grid[i][j]
                    elif j==n-1:
                        mat[i+1][0]=grid[i][n-1]
            grid=mat
        return grid           
        