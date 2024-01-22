class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        forward = 0
        after = len(nums) - 1
        while forward < after :
            if nums[forward] % 2 == 1 and nums[after] % 2 == 0:
                nums[forward], nums[after] = nums[after], nums[forward]
            if nums[forward] % 2 == 0:
                forward += 1
            if nums[after] % 2 == 1:
                after -= 1
        return nums
        