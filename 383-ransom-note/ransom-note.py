class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 透過record記錄 magazine裡各個字元出現次數
        record = {char: magazine.count(char) for char in set(magazine)}
        # print(record)
        for c in ransomNote:
            if not c in record or record[c] == 0:
                return False
            else:
                record[c]-=1
        return True

