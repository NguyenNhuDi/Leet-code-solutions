class Solution:

    def count_ones(self, n):
        out = 0
        while n != 0:
            if n % 2:
                out += 1
            n //= 2
        return out


    def sortByBits(self, arr: List[int]) -> List[int]:

        toSort = [(self.count_ones(i), i) for i in arr]
        toSort.sort()

        out = [i[1] for i in toSort]
        return out
    
