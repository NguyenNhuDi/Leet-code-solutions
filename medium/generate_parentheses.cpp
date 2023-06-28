class Solution {
public:
    
    
    void gen_arr(int i, vector<vector<string>> & dp, int stop){
        if(i == stop){
            return;
        }

        if(i == 0){
            dp[0].push_back("()");
        
            gen_arr(i + 1, dp,stop);
            return;
        }

        vector<string> temp = dp[i-1];

        for(const auto & x : temp){

            for(int j = 0; j < x.size(); j++){
                dp[i].push_back(x.substr(0,j)+"()"+x.substr(j));
            }
        }

        gen_arr(i+1,dp,stop);
    }

    vector<string> generateParenthesis(int n) {
        vector<vector<string>> dp(8);
        gen_arr(0,dp,n);

        unordered_set<string> fred;
        vector<string> out;

        for(const auto & x : dp[n-1]){
            if(fred.count(x) == 0){
                out.push_back(x);
                fred.insert(x);
            }
        }

        return out;
    }


};
