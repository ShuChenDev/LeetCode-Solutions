/*
12/1/2024
Mathematic
*/

class Solution {
public:
    int nthUglyNumber(int n) {
        if(n == 0) return 0;
        if(n == 1) return 1;

        vector<int> seq(n);
        seq[0] = 1;
        int n2 = 0;
        int n3 = 0;
        int n5 = 0;

        for(int i = 1; i < n; i++) {
            seq[i] = (min(seq[n2] * 2, min(seq[n3] * 3, seq[n5] * 5)));
            if(seq[i] == seq[n2] * 2) n2++;
            if(seq[i] == seq[n3] * 3) n3++;
            if(seq[i] == seq[n5] * 5) n5++;
        }

        return seq[n-1];
    }
};
