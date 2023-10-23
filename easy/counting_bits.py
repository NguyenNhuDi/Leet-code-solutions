class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]

        counter = 0
        prev = 1
        for i in range(1,n+1):
            if i == prev * 2:
                prev *= 2
                counter = 0
            dp[i] = dp[counter] + 1
            counter += 1

        return dp 
