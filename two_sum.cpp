//Two Sum
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<unordered_set>
#include<cmath>
#include<climits>
#include<queue>
#include<stack>
#include<map>
#include<unordered_map>

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define FORD(i,a,b) for(int i = a; i >= b; i--)
#define FORE(i,a,b) for(int i = a; i <=b; i++)
#define foreach(x,y) for(const auto & x : y)
#define SIZE(x) x.size()
#define vi vector<int>
#define usi unordered_set<int>
#define si set<int>
#define MOD 0x3b9aca07

using namespace std;

class Solution {
public:

    static bool sortVectorPair(pair<int,int> a, pair<int,int> b){
        return a.first < b.first;
    }

    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        vector<pair<int,int>> input(n);
        
        //O(n)
        for(int i = 0; i < n; i++){
            pair<int,int> temp(nums[i], i);
            input[i] = temp;
        }

        sort(input.begin(), input.end(),sortVectorPair);
        vector<int> out(2);

        int l = 0;
        int r = n - 1;
        while(r > l){

            int currNum = input[l].first + input[r].first;

            if(currNum == target){
                out[0] = input[l].second;
                out[1] = input[r].second;
                return out;
            }
            else if(currNum > target){
                r--;
            }
            else{
                l++;
            }
        }

        return out;

    }
};

int main(){

    Solution test = Solution();


    int n, target; cin >> n >> target;

    vi t(n);

    FOR(i,0,n){
        cin >> t[i];
    }


    foreach(x,test.twoSum(t,target)){
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
