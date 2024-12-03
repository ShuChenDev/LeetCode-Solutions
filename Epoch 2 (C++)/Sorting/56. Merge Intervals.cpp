    /*
    12/2/2024
    Sort
    */

    class Solution {
    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            if(intervals.size() <= 1) {
                return intervals;
            }

            sort(intervals.begin(), intervals.end());
            vector<vector<int>> rtn;
            
            rtn.push_back(intervals[0]);

            for(int i = 1; i < intervals.size(); i++) {
                if(rtn.back()[1] >= intervals[i][0]) {
                    rtn.back()[1] = max(rtn.back()[1], intervals[i][1]);
                }
                else {
                    rtn.push_back(intervals[i]);
                }
            }

            return rtn;
        }
    };
