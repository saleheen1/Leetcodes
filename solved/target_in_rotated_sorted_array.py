class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left = 0
        n = len(nums)
        right = n -1
        min_index = 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_index = left

        # finding in which portion does the target is 
        if min_index == 0:
            left = 0
            right = n - 1
        elif target >= nums[0] and target <= nums[min_index -1]:
            left, right = 0, min_index -1
        else:
            left,right = min_index, n - 1

        # Doing a binary search in that portion where target may be
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        
        return -1
            

        

    
s =Solution()
print(s.search(nums=[4,5,7,8,0,1,2],target=2))
