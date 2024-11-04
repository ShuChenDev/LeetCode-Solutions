/*
11/4/2024
Hash Map
*/

class Solution {
public:
    int romanToInt(string s) {
        
        if (s.size() == 0) {
            return 0;
        }

        unordered_map<char,int> symbol;
        symbol['I'] = 1;
        symbol['V'] = 5;
        symbol['X'] = 10;
        symbol['L'] = 50;
        symbol['C'] = 100;
        symbol['D'] = 500;
        symbol['M'] = 1000;

        int sum = 0;
        int temp = 0;
        sum = sum + symbol[s[0]];

        for(int i = 1; i < s.size(); i++) {
            if (symbol[s[i]] > symbol[s[i-1]]) {
                sum = sum - 2*symbol[s[i-1]];
            }
                sum = sum+symbol[s[i]];
        }

        return sum;
    }
};
