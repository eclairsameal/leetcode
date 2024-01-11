class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        arr_len = len(arr)
        for n in arr:
            if n == 0:
                res.extend([0]*2)
            else :
                res.append(n)
            if len(res) >= arr_len:
                arr[:] = res[:arr_len]   
                break