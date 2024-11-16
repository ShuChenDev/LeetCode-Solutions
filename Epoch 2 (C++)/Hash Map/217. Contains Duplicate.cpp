/*
11/16/2024
Hash Map
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> used;
        for(int i = 0; i < nums.size(); i++)
        {
            if(used[nums[i]] == true)
            {
                return true;
            }
            used[nums[i]] = true;
        }
        return false;
    }
};
