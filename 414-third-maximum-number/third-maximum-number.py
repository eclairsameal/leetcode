class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = sorted(set(nums), reverse=True)
        return l[2] if len(l) >= 3 else l[0]