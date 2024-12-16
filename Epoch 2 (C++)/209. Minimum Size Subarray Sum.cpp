/*
12/16/2024
Two Pointers
*/

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        if (target == 0) return 0;

        int rtn = nums.size()+1;
        int left = 0;
        int cur = 0;

        for(int i = 0; i < nums.size(); i++) {
            cur += nums[i];
            while (cur >= target) {
                rtn = min(rtn, i-left+1);
                cur = cur - nums[left];
                left++;
            }
        }
        

        if(rtn == nums.size()+1) return 0;
        return rtn;
    }
};
