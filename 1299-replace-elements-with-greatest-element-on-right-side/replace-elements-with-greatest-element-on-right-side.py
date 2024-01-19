class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = arr[len(arr)-1]
        temp = 0
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = r
            r = max(temp, r)
        arr[len(arr)-1] = -1
        return arr
