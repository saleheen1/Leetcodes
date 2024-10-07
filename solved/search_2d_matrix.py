class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        oneDLeft = 0
        oneDRight = len(matrix) -1
        valueMaybeIn = []

        twoDLeft = 0
        twoDRight = 0
        

        while oneDLeft <= oneDRight:
            oneDMid = (oneDLeft + oneDRight) // 2

            if target > matrix[oneDMid][-1]:
                oneDLeft = oneDMid +1
            elif target < matrix[oneDMid][0]:
                oneDRight = oneDMid -1
            else:
                valueMaybeIn = matrix[oneDMid]
                break

        
        twoDRight = len (valueMaybeIn) -1

        while twoDLeft <= twoDRight:
            mid = (twoDLeft+twoDRight) // 2
            
            if valueMaybeIn[mid] < target:
                twoDLeft = mid+1
            elif valueMaybeIn[mid] > target:
                twoDRight = mid -1
            else:
                return True
        
        return False
            








s =Solution()
print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],target = 73))

