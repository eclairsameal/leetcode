func findDisappearedNumbers(nums []int) []int {
    ans := []int{}
    for _, x := range nums {
        i := abs(x) - 1
        if nums[i] > 0 {
            nums[i] = -nums[i]
        }
    }
    for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			ans = append(ans, i+1)
		}
	}
	return ans
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
