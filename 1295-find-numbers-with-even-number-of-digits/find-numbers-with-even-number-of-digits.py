class Solution:
    
    def findNumbers(self, nums: List[int]) -> int:
        res = map(lambda x: 1 if len(str(x)) % 2 == 0 else 0, nums)
        return sum(res)
    

    
