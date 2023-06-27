class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return x

        int_max = 2147483647
        int_min = -2147483648

        negative = True if x < 0 else False

        x = abs(x)
        out = 0
        while x != 0:
            out = (x % 10) + out * 10
            x //= 10


        if negative:
            out *= -1

        if out < int_min or out > int_max:
            return 0
        
        return out
