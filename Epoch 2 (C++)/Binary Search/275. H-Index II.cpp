/*
12/19/2024
Binary Search
*/

class Solution {
public:
    int hIndex(vector<int>& citations) {

        int left = 0;
        int right = citations.size()-1;
        
        while(left <= right) {
            int mid = (left + right) / 2;
            if(citations[mid] == citations.size() - mid) return citations[mid];
            else if(citations[mid] > citations.size() - mid) right = mid - 1;
            else left = mid + 1;
        }
 
        return citations.size() - right - 1;
    }
};
