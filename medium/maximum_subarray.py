class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = -2147483648
        curr = out

        for i in nums:
            curr = max(curr + i, i)
            out = max(out, curr)

        return out
