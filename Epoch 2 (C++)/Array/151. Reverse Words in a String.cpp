/*
12/26/2024
Array
*/

class Solution {
public:
    string reverseWords(string s) {
        string rtn = "";
        string temp = "";

        for(int i = s.size()-1; i >= 0; i--) {
            if(s[i] == ' ') {
                if(rtn != "") rtn = rtn + " ";
          
                rtn = rtn + temp;
                temp = "";
          
                while(i > 0 && s[i] == ' ') i--;
            }
            temp = s[i] + temp;
        }

        if(rtn == "") rtn = temp;
        else if(temp != " ") rtn = rtn + " " + temp;
        
        return rtn;
    }
};
