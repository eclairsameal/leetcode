class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = [sum(account) for account in accounts]
        return max(sum_list)