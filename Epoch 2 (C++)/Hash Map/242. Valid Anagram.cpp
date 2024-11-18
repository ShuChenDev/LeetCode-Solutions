/*
11/18/2024
Hash Map
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> letter;

        if(s.size() != t.size()) {
            return false;
        }

        for(int i = 0; i < s.size(); i++) {
            letter[s[i]]++;
        }
        for(int i = 0; i < t.size(); i++) {
            if (letter.find(t[i]) == letter.end() || letter[t[i]] == 0) {
                return false;
            }
            letter[t[i]]--;
        }
        return true;
    }
};
