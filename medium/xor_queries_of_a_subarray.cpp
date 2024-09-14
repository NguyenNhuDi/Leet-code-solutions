#define q(x) queries[i][x]

class Solution {
public:

    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> out(queries.size());

        for(int i = 0; i < queries.size(); i++){
            int l = q(0), r = q(1);
            if (l == r)
                out[i] = arr[l];
            else{
                int ans = arr[l];
                for(int j = l + 1; j <= r; j ++)
                    ans ^= arr[j];
                out[i] = ans;
            }
        }

        return out;
    }
};
