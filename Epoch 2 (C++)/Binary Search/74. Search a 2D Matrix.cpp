/*
12/11/2024
Binary Search
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int left = 0;
        int right = matrix.size()-1;
        int mid;

        while(left <= right) {
            mid = (left + right) / 2;
            
            if(matrix[mid][0] > target) {
                right = mid - 1;
            }
            else if(matrix[mid][matrix[mid].size()-1] < target) {
                left = mid + 1;
            }
            else {
                left = 0;
                right = matrix[mid].size()-1;
                
                while(left <= right) {
                    int m = (left + right) / 2;
                    if(matrix[mid][m] < target) {
                        left = m + 1;
                    }
                    else if(matrix[mid][m] > target) {
                        right = m - 1;
                    }
                    else {
                        return true;
                    }
                }

                return false;
            }
        }

        return false;
    }
};
