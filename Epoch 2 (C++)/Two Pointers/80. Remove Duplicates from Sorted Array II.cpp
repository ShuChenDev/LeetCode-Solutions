/*
12/21/2024
Two Pointers
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if(nums.size() <= 2) return nums.size();
        
        int left = 2;
        for(int i = 2; i < nums.size(); i++) {
            if(nums[i] != nums[left-2]) {
                nums[left] = nums[i];
                left++;
            }
        }

        return left;
    }
};
