/*
11/24/2024
Hash Map
*/

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        for(int i = 0; i < board[0].size(); i++) {
            set<char> nums1;
            set<char> nums2;
            set<char> nums3;

            for(int j = 0; j < board[0].size(); j++) {
                if(nums1.find(board[i][j]) == nums1.end()) {
                   if(board[i][j] != '.') {
                        nums1.insert(board[i][j]);
                    }
                }
                else return false;
                
                if(nums2.find(board[j][i]) == nums2.end()) {
                    if(board[j][i] != '.' ) {
                        nums2.insert(board[j][i]);
                    }
                }
                else return false;

                if(nums3.find(board[3 * (i / 3) + j / 3][3 * (i % 3) + j % 3]) == nums3.end()) {
                    if(board[3 * (i / 3) + j / 3][3 * (i % 3) + j % 3] != '.') {
                        nums3.insert(board[3 * (i / 3) + j / 3][3 * (i % 3) + j % 3]);
                    }
                }
                else return false;
            }
        }
        return true;
    }
};
