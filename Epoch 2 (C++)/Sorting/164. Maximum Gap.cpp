/*
12/6/2024
Sorting
*/

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if(nums.size() < 2) return 0;
        
        sort(nums.begin(), nums.end());
        int rtn = 0;
        for(int i = 1; i < nums.size(); i++) {
            rtn = max(rtn, nums[i] - nums[i-1]);
        }

        return rtn;
    }
};
