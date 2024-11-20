
/*
11/20/2024
Hash Map
*/

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char,string> word;
        unordered_map<string,char> letter;

        string temp = "";
        s += ' ';

        int j = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == ' ') {
                if(word.find(pattern[j]) == word.end()) {
                    word[pattern[j]] = temp;
                }
                else if (word[pattern[j]] != temp) {
                    return false;
                }
                if(letter.find(temp) == letter.end()) {
                    letter[temp] = pattern[j];
                }
                else if (letter[temp] != pattern[j]) {
                    return false;
                }

                temp = "";
                j++;
            }
            else {
                temp += s[i];
            }
        }

        if(j != pattern.size()) {
            return false;
        }

        return true;
    }
};
