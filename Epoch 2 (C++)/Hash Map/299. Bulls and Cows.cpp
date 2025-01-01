/*
Hash Map
1/1/2025
*/

class Solution {
public:
    string getHint(string secret, string guess) {
        int bull = 0;
        int cow = 0;

        unordered_map<char, int> map;
        
        for(int i = 0; i < secret.size(); i++) {
            map[secret[i]]++;
        }
        
        for(int i = 0; i < secret.size(); i++) {
            if(guess[i] == secret[i]) {
                bull++;
                if(map[secret[i]] > 0) {
                    map[secret[i]]--;
                }
                else {
                    cow--;
                }
            }
            else if(map.find(guess[i]) != map.end() && map[guess[i]] > 0) {
                cow++;
                map[guess[i]]--;
            }
        }

        return to_string(bull) + "A" + to_string(cow) + "B";
    }
};
