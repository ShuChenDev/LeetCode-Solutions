/*
12/13/2024
Binary Search
*/

class Solution {
public:
    int findMin(vector<int>& nums) {
        
        int left = 0;
        int right = nums.size() - 1;

        while(left < right) {
            int mid = (left + right) / 2;
        
            if(nums[mid] <= nums[right]) {
                if(mid == left || nums[mid-1] >= nums[mid]) {
                    return nums[mid];
                }
                else {
                    right = mid-1;
                }
            }
            else {
                left = mid+1;
            }
        }

        return nums[left];
    }
};
