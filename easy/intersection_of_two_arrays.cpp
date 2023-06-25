class Solution {
public:

    int bSearch(int l, int r, int x, vector<int> & arr){
        if (l>=r){
            return -1;
        }

        int m = (l + r)/2;

        if(arr[m] == x){
            return m;
        }
        //x is to the left
        else if(x < arr[m]){
            return bSearch(l,m,x,arr);
        }
        //x is to the right
        else{
            return bSearch(m+1,r,x,arr);
        }
    }

    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        //sort nums2 to use bSearch
        sort(nums2.begin(), nums2.end());

        vector<int> out;
        unordered_set<int> fred;
        int r = nums2.size();
        for(const int & i: nums1){
            if(bSearch(0,r,i,nums2) >= 0 && fred.find(i) == fred.end()){
                out.push_back(i);
                fred.insert(i);
            }
        }

        return out;

    }
};
