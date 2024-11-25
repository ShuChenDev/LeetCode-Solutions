/*
11/24/2024
Hash Map
*/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        vector<vector<string>> rtn;

        for(int i = 0; i < strs.size(); i++) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            m[temp].push_back(strs[i]);
        }

        for(auto i : m) {
            rtn.push_back(i.second);
        }

        return rtn;
    }
};
