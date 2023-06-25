class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> m;

        if(s.size() == 0){
            return 0;
        }

        if(s.size() == 1){
            return 1;
        }

        int out = 0;
        int cIndex = 0;
        int i = 0;
        for (i; i < s.size(); i++){

            char curr = s[i];

            //if its not in the map alr
            if(m.find(curr) == m.end()){
                m[curr] = i;
            }
            //if its behind the current cut off
            else if(m[curr] < cIndex){
                m[curr] = i;
            }
            //if the repeat is ahead
            else{
                cIndex = m[curr] + 1;
                m[curr] = i;
            }

            out = max(out, i - cIndex+1);
        }
        return out;
    }
};
