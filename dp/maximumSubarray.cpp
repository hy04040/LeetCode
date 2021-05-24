class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current = nums[0];
        int len = nums.size();
        int max = nums[0];
        for(int i=1; i<len; i++){
            if(current < 0)
                current = 0;
            current += nums[i];
            if(max < current)
                max = current;
        }
        return max;
    }
};