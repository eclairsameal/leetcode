class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> sort_heights = heights;
        int times = 0;
        sort(sort_heights.begin(), sort_heights.end());

        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != sort_heights[i]) {
                times++;
            }
        }
        return times;
    }
};