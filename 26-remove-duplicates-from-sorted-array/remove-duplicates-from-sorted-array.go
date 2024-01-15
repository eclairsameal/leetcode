func removeDuplicates(nums []int) int {
    i, j := 1, 1
    for i < len(nums) {
        if nums[i-1] != nums[i] {
            nums[j]=nums[i];
            j++;
        }
        i++
    }
    return j;
}
