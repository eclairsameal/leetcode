int removeDuplicates(int* nums, int numsSize) {
    int res = 0, check_number = 0;
    for (int i = 0; i < numsSize; i++) {
        if (check_number != nums[i] || i == 0) {
            check_number = nums[i];
            nums[res] = check_number;
            res++;
        }
    }
    return res;
}