class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 : return False
        arr_len = len(arr)
        left, right = 0, arr_len - 1

        while left < arr_len - 1 and arr[left] < arr[left +1]:
            left += 1
        while right > 0 and arr[right] < arr[right -1] :
            right -= 1
        return right == left and right != 0 and left != (arr_len-1)