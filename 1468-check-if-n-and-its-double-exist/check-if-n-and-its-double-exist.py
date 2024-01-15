class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for n in arr:
            if n*2 in arr and n != 0: 
                return True
            elif arr.count(0) >= 2:
                return True
        return False