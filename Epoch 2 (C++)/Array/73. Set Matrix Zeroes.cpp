/*
11/25/2024
Array
*/

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>> zeros;

        int n1 = matrix.size();
        int n2 = matrix[0].size();

        for(int i = 0; i < n1; i++) {
            for(int j = 0; j < n2; j++) {
                if(matrix[i][j] == 0) {
                    zeros.push_back({i,j});
                }
            }
        }

        for(int i = 0; i < zeros.size(); i++) {
            for(int j = 0; j < n2; j++) {
                matrix[zeros[i][0]][j] = 0;
            }
            for(int k = 0; k < n1; k++) {
                matrix[k][zeros[i][1]] = 0;
            }
        }

    }
};
