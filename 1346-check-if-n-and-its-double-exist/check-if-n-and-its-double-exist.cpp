class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        // hash table
        set<int> set_map;
        for (int num : arr) {
            // 迭代數組並檢查數組中的元素乘以 2 或除以 2 是否等於物件中的元素Set。
            if (set_map.count(num * 2) || (num % 2 == 0 && set_map.count(num / 2))) return true;
            set_map.insert(num);
        }
        return false;
    }
};