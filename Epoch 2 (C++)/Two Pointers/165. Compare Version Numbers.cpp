/*
12/27/2024
Two Pointers
*/

class Solution {
public:
    int compareVersion(string version1, string version2) {
        int left = 0;
        int right = 0;
        int l = 0;
        int r = 0;

        while(l < version1.size() || r < version2.size()) {
            left = 0;
            while(l < version1.size() && version1[l] != '.') {
                left = left * 10 + (version1[l] - '0');
                l++;
            }
            l++;

            right = 0;
            while(r < version2.size() && version2[r] != '.') {
                right = right * 10 + (version2[r] - '0');
                r++;
            }
            r++;

            if(left < right) return -1;
            if(left > right) return 1;
            left = 0;
            right = 0;
        }
        return 0;
    }
};
