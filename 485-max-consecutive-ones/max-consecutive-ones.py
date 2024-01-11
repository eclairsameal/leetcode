class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        resule = 0
        sum = 0
        for n in nums:
            sum = (sum + n) * n
            resule = max(sum, resule)
        return resule