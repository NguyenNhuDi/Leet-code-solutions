class Solution {
public:
    int reverse(int x) {
        if(x == 0){
            return 0;
        }
        
        long long int_max = 2147483647;
        long long int_min = -2147483648;


        long long y = (long long)x;

        bool negative = y < 0 ? true : false;

        y = abs(y);

        long long out = 0;
        while (y != 0){
            out = (y % 10) + out * 10;
            y /= 10;
        }

        if (negative){
            out *= -1;
        }

        if(out < int_min || out > int_max){
            return 0;
        }

        return (int) out;


    }
};
