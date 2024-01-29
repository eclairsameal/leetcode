class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_max = max(heights)
        heights_min = min(heights)
        index = 0
        times = 0
        count_list = [0] * (heights_max - heights_min + 1)
        for i in range(len(heights)):
            count_list[heights[i] - heights_min ]+=1
        for i in range(len(count_list)):
            while count_list[i] > 0:
                if heights[index] != i + heights_min:
                    times += 1
                count_list[i] -= 1
                index +=1 
        return times
        