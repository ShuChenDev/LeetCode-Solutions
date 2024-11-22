/*
11/22/2024
Hash Map
*/

class Solution {
public:
    string intToRoman(int num) {
        
        unordered_map<int, pair<string, string>> symbol = {
            {1, {"I", "V"}},
            {2, {"X", "L"}},
            {3, {"C", "D"}},
            {4, {"M", "M"}}
        };

        string rtn = "";
        int digit = 0;

        while(num != 0) {
            int i = num % 10;
            num = num / 10;
            digit++;

            if(i == 4) {
                rtn = symbol[digit].first + symbol[digit].second + rtn;
            }
            else if(i == 9) {
                rtn = symbol[digit].first + symbol[digit+1].first + rtn;
            }
            else {
                string temp = "";
                temp.append(i / 5, symbol[digit].second[0]);
                temp.append(i % 5, symbol[digit].first[0]);
                rtn = temp + rtn;
            }
        }
        return rtn;
    }
};
