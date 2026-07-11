class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        seen=[]
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                    
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        
sol=Solution()
sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])