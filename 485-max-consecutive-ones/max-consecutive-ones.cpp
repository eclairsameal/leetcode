class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int resule = 0, sum = 0;
        for (auto x: nums) {
            sum = (sum + x) * x;
            if (sum > resule) {
                resule = sum;
            }
        }
        return resule;
    }
};