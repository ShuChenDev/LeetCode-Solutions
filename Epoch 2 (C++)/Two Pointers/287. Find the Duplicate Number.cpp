/*
Two Pointers
12/18/2024
*/

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = nums[0];
        int right = nums[nums[0]];

        while(left != right) {
            left = nums[left];
            right = nums[nums[right]];
        }
        
        left = 0;
        
        while(left != right) {
            left = nums[left];
            right = nums[right];
        }
        return left;
    }
};
