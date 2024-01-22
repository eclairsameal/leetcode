class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int forward = 0;
        int after = nums.size() - 1;
        while (forward < after) {
            if (nums[forward] % 2 == 1 && nums[after] % 2 == 0) {
                int temp = nums[forward];
                nums[forward] = nums[after];
                nums[after] = temp;
                forward++;
                after--;
            }
            if (nums[forward] % 2 == 0 ) {
                forward++;
            }
            if (nums[after] % 2 == 1) {
                after--;
            }
        }
        return nums;
    }
};