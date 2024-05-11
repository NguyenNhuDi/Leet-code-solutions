class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        
        l, r = 0, len(height) - 1
        

        maxi = -1

        while l != r:
            h1 = min(height[l], height[r])
            w1 = r - l

            maxi = max(maxi, h1 * w1)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1


        return maxi
