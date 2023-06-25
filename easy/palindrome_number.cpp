//Palindrome Number

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
    bool isPalindrome(int x) {
        string t = to_string(abs(x));

        return t[0] == t[t.size()-1] ? true : false;


    }
};


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Solution t = Solution();

    int n; cin >> n;
    cout << t.isPalindrome(n) << endl;

    return 0;
}
