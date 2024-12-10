/*
12/10/2024
Sorting
*/

class Solution {
public:
    int hIndex(vector<int>& citations) {
        
        vector<int> rtn(citations.size() + 1, 0);
        
        for(int i : citations) {
            if(i >= citations.size()) rtn[citations.size()]++;
            else rtn[i]++;
        }

        int temp = 0;
        for(int i = citations.size(); i >= 0; i--) {
            temp += rtn[i];
            if(temp >= i) return i;
        }

        return 0;
    }
};
