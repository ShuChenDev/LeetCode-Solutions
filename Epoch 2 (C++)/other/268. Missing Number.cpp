/*
11/19/2024
Mathematical
*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int rtn = nums.size();
        for(int i = 0; i < nums.size(); i++) {
            rtn += i - nums[i];
        }
        return rtn;
    }
};
