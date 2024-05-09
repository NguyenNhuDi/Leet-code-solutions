class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        out = [['' for i in range(1000)] for j in range(numRows)]
        
        row, col = 0, 0
        rev = False

        for c in s:

            out[row][col] = c

            if not rev:
                row += 1
            else:
                row -= 1
                col += 1

            if row >= numRows - 1:
                rev = True

            if row == 0:
                rev = False

        ans = ''

        for row in out:
            for c in row:
                ans += c

        return ans
                
            
