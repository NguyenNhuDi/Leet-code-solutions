class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        minLen = 201
        for s in strs:
            minLen = min(minLen, len(s))

        for i in range(minLen, -1, -1):
            curr = strs[0][:i]
            val = True

            for s in strs:
                if s[:i] != curr:
                    val = False
                    break
            
            if val:
                return curr
        
        return ''
