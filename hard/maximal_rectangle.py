class Solution:
    def maximalRectangle(self, matrix) -> int:
        width = len(matrix[0])
        height = len(matrix)
        dp = [[-1 for j in range(width)] for i in range(height)]
        for y in reversed(range(height)):
            for x in reversed(range(width)):
                if x == width - 1:
                    dp[y][x] = int(matrix[y][x])
                else:
                    dp[y][x] = dp[y][x+1] + 1 if int(matrix[y][x]) == 1 else 0  
            
        out = 0
        for x in range(width):
            for y in range(height):
                mW = dp[y][x]
                _y = y
                i = 1
                while _y < height and dp[y][x] > 0:
                    mW = min(mW, dp[_y][x])
                    out = max(out, mW * (i))
                    i += 1
                    _y += 1
        return out

