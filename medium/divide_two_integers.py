class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -2147483648
        int_max = 2147483647
        #xor since if both neg or both pos it will be false
        negative = (dividend < 0) ^ (divisor < 0)
        #the idea here is that a/b = e^(ln(a) - ln(b))
        a = abs(dividend)
        b = abs(divisor)

        if b == 1:
            out = -a if negative else a

            if out < int_min:
                return int_min
            elif out > int_max:
                return int_max
            else:
                return out
        if b > a:
            return 0

        out = floor(math.exp(math.log(a) - math.log(b)) +  0.0000000001)


        out = -out if negative else out

        if out < int_min:
            return int_min
        elif out > int_max:
            return int_max
        else:
            return out
            
