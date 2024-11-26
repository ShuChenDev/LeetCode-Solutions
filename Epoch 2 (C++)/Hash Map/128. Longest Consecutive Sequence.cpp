/*
11/26/2024
Hash Map
*/

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int rtn = 0;
        
        unordered_set<int> set;
        for(auto i : nums) {
            set.insert(i);
        }
        
        for(auto i : nums) {
            int temp = 0;

            if(set.find(i-1) == set.end()) {
                while(set.find(i+temp) != set.end()) {
                    temp++;
                }    
            }
            
            rtn = max(rtn, temp);
        }
        
        return rtn;
    }
};
