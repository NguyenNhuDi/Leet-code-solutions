class Solution:

    def bSearch(self, l, r, x, arr, last, left):
        if l >= r:
            if left:
                return last 
            else:
                return last + 1
        
        m = (l + r) // 2

        if x == arr[m]:
            return m
        # x is to the left
        elif x < arr[m]:
            return self.bSearch(l,m,x,arr,m,True)
        else:
            return self.bSearch(m+1,r,x,arr,m,False)


    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bSearch(0,len(nums),target,nums,-1,False)
