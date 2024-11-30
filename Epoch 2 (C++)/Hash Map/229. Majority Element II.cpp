/*
11/30/2024
Hash Map
*/

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;
        int t = nums.size()/3;
        vector<int> rtn;
        
        for(int i : nums) {
            count[i]++;
            if(count[i] > t && find(rtn.begin(), rtn.end(), i) == rtn.end()) {
                rtn.push_back(i);
            }
        }

        return rtn;
    }
};
