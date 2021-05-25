class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        int dp[101][101] = {0};
        if(obstacleGrid[0][0] != 1)
            dp[0][0] = 1;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 && obstacleGrid[i][j] != 1 && j>0 && obstacleGrid[i][j-1] != 1){
                    dp[i][j] = dp[i][j-1];
                }else if(j==0 && obstacleGrid[i][j] != 1 && i>0 && obstacleGrid[i-1][j] != 1){
                    dp[i][j] = dp[i-1][j];
                }else if(i>0 && j>0 && obstacleGrid[i][j] != 1){ 
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
               }
            }
        }
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++)
                cout << dp[i][j] << " ";
            cout << endl;
        }
        return dp[m-1][n-1];
    }
};