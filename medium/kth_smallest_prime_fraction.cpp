class Solution {
private:
struct node{
    double value;
    int top, bot;

    bool operator <(const node & a) const{
        return value < a.value || (value == a.value && top < a.top || (top == a.top && bot < a.bot));
    }
};


public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        set<node> prioQueue;

        for(int i = 0; i < arr.size() - 1; i++){
            for(int j = i+1; j < arr.size(); j++ ){
                node temp;
                temp.value = (double) arr[i] / (double) arr[j];
                temp.top = arr[i];
                temp.bot = arr[j];
                prioQueue.insert(temp);

                if (prioQueue.size() > k){
                    auto it = prioQueue.end();
                    it--;
                    prioQueue.erase(it);
                }
            }
        }
        
        auto it = prioQueue.end();
        it--;

        return {it->top, it->bot};

    }
};
