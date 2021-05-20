class Solution {
public:
    string longestPalindrome(string s) {
        int dp[1001][1001] = {0};
        int len = s.length();
        string answer = "";
        for(int i=1; i<len+1; i++){
            for(int j=0; j<len-i+1; j++){
                if(i==1 || (i==2 && s.at(j) == s.at(j+1)) || (dp[i-2][j+1] ==1 &&(s.at(j) == s.at(j+i-1)))){
                    dp[i][j] = 1;
                    answer = s.substr(j,i);
                }
            }
        }
        return answer;
    }
};