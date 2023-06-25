class Solution {
public:
    bool isValid(string s) {
        stack<char> fred;

        for(const char & i : s){
            if (fred.size() == 0){
                if(i == ']' || i == ')' || i== '}'){
                    return false;
                }

                fred.push(i);
            }
            else{
                char tos = fred.top();

                if(tos == '['){
                    if(i ==']'){
                        fred.pop();
                    }
                    else if (i =='}' || i == ')'){
                        return false;
                    }
                    else{
                        fred.push(i);
                    }
                }
                else if(tos=='{'){
                    if(i =='}'){
                        fred.pop();
                    }
                    else if (i ==']' || i == ')'){
                        return false;
                    }
                    else{
                        fred.push(i);
                    }
                }
                else{
                    if(i ==')'){
                        fred.pop();
                    }
                    else if (i =='}' || i == ']'){
                        return false;
                    }
                    else{
                        fred.push(i);
                    }
                }
            

            }
        }

        return fred.size() == 0 ? true : false;

    }
};
