func sortArrayByParity(nums []int) []int {
    forward, after := 0, len(nums) - 1
    for forward < after {
        if nums[forward] % 2 == 1 && nums[after] % 2 == 0 {
            nums[forward], nums[after] = nums[after], nums[forward]
        }
        if nums[forward] % 2 == 0 {
            forward++
        }
        if nums[after] % 2 == 1 {
            after--
        }
    }
    return nums
}