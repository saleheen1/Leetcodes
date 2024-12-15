class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal:
                goal = i

        return goal == 0