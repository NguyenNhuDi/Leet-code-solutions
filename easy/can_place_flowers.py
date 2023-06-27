class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)

        if size == 1:

            if n == 0:
                return True

            return True if flowerbed[0] == 0 else False

        i = 0
        prev = 0
        while i < size - 1 and n > 0:
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

            prev = flowerbed[i+1]
            i += 2
            
        if flowerbed[-2] == 0 and flowerbed[-1] == 0 and n > 0:
                flowerbed[-1] = 1
                n -= 1
        
        return True if n == 0 else False
