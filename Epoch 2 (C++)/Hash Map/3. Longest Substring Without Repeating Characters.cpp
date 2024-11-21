/*
11/21/2024
Hash Map
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        if(s.size() < 1) {
            return 0;
        }

        unordered_map<char,int> map;

        int rtn = 1;
        int left = 0;
        int right = 1;

        map[s[left]]++;

        while (right < s.size()) {
            map[s[right]]++;
            while(map[s[right]] > 1) {
                map[s[left]]--;
                left++;
            }
            right++;
            rtn = max(rtn, right - left);
        }
        return rtn;
    }
};
