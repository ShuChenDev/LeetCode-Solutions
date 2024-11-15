/*
11/15/2024
Hash Map
*/

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }
        
        unordered_map<char, char> schart;
        unordered_map<char, char> tchart;
        
        for(int i = 0; i < s.size(); i++)
        {
            if(schart.find(s[i]) != schart.end())
            {
                if(schart[s[i]] != t[i])
                {
                    return false;
                }
            }
            else
            {
                schart[s[i]] = t[i];
            }
            
            if(tchart.find(t[i]) != tchart.end())
            {
                if(tchart[t[i]] != s[i])
                {
                    return false;
                }
            }
            else
            {
                tchart[t[i]] = s[i];
            }

        }
        return true;
    }
};
