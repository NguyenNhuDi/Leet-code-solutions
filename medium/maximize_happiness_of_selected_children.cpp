class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater());

        long long out = 0, dec = 0;
        for(int i = 0; i < k; i++){
            out += happiness[i] - dec >= 0 ? happiness[i] - dec : 0;
            dec++; 
        }

        return out;

    }
};
