func removeElement(nums []int, val int) int {
    lenght := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != val {
            nums[lenght] = nums[i]
            lenght++
        }
    }
    return lenght
}