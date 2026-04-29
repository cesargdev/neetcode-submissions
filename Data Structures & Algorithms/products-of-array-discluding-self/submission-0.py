class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        output = [1] * n

        # nums = [1,2,3,4]
        # left = [1,1,2,6]
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        
        # right = [24,12,4,1]
        for i in reversed(range(n-1)):
            right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            output[i] = left[i]*right[i]
        return output
        