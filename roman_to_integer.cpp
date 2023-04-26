//Roman to Integer
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<unordered_set>
#include<cmath>
#include<climits>
#include<queue>
#include<map>

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define FORD(i,a,b) for(int i = a; i >= b; i--)
#define FORE(i,a,b) for(int i = a; i <=b; i++)
#define SIZE(x) x.size()
#define vi vector<int>
#define usi unordered_set<int>
#define si set<int>
#define MOD 0x3b9aca07

using namespace std;


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int out = 0;
    int len = SIZE(s);
    FOR(i,0,len){
        if(s[i] == 'I'){
            if(s[i+1] == 'V'){
                out += 4;
                i++;
            }
            else if(s[i + 1] == 'X'){
                out += 9;
                i++;
            }
            else{
                out++;
            }
        }
        else if (s[i] == 'V'){
            out += 5;
        }
        else if (s[i] == 'X'){
            if(s[i+1] == 'L'){
                out += 40;
                i++;
            }
            else if(s[i + 1] == 'C'){
                out += 90;
                i++;
            }
            else{
                out += 10;
            }
              
        }
        else if(s[i] == 'L'){
            out += 50;
        }
        else if(s[i] == 'C'){
            if(s[i+1] == 'D'){
                out += 400;
                i++;
            }
            else if(s[i + 1] == 'M'){
                out += 900;
                i++;
            }
            else{
                out += 100;
            }         
        }
        else if(s[i] == 'D'){
            out += 500;
        }
        else{
            out += 1000;
        }
    }
    cout << out << endl;

    return 0;
}
