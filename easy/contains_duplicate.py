class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> fred;

        for(const auto & i: nums){
            if(fred.count(i)){
                return true;
            }
            else{
                fred.insert(i);
            }
        }

        return false;

    }
};
