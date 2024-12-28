/*
12/28/2024
Two Pointers
*/

class Solution {
public:
    void rev(vector<int>& nums, int start, int end) {
        int left = start;
        int right = end;

        while(left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
    
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        rev(nums, 0, nums.size() - k - 1);
        rev(nums, nums.size() - k, nums.size()-1);
        rev(nums, 0, nums.size() - 1);
    }
};
