/*
11/29/2024
Hash Map
*/

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if(s.size() < 10) {
            return {};
        }
        
        vector<string> rtn;
        unordered_set<string> pre;

        pre.insert(s.substr(0, 10));

        int left = 1;

        for(; left + 9 < s.size(); left++) {
            string cur = s.substr(left, 10);

            if(pre.find(cur) != pre.end() && find(rtn.begin(), rtn.end(), cur) == rtn.end()) {
               rtn.push_back(cur);
            }
            else {
                pre.insert(cur);
            }
        }

        return rtn;
    }
};
