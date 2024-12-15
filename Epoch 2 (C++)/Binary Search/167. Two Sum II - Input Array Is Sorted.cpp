/*
12/15/2024
Binary Search
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        for(int i = 0; i < numbers.size(); i++) {
            int tar = target - numbers[i];
            int left = i+1;
            int right = numbers.size()-1;

            while(left <= right) {
                int mid = (left + right) / 2;
                if(numbers[mid] > tar) right = mid-1;
                else if(numbers[mid] < tar) left = mid+1; 
                else return {i+1, mid+1};
            }
        }
        return {0, 0};
    }
};
