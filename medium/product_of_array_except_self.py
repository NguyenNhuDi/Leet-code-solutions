class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
       
        out = [1 for i in range(n)]
       
        t = 1

        for i in range(n):
            out[i] = t
            t *= nums[i]

        t = 1

        for i in reversed(range(n)):
            out[i] *= t
            t *= nums[i]
        return out
       
