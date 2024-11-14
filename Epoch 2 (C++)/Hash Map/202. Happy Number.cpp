/*
11/14/2024
Hash Map
*/

class Solution {
public:
    bool isHappy(int n) {  
        
        int num = 0;
        unordered_set<int> numMap;

        while (num != 1 && numMap.find(n) == numMap.end())
        {
            numMap.insert(n);
            num = 0;
            while (n>0)
            {
                num = num + (n%10)*(n%10);
                n = n/10;       
            }
            n = num;
        }   
        return n == 1;    

    }
};
