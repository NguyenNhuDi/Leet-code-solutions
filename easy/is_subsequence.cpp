class Solution {
public:
    bool isSubsequence(string s, string t) {
        int counter = 0;

        for(const auto & x : t) if(s[counter] == x) counter++;

        return counter == s.size() ? true : false;
    }
};
