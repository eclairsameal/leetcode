bool canConstruct(char* ransomNote, char* magazine) {
    // 透過record記錄 magazine裡各個字元出現次數
    int record[26] = {0};
    for (int i = 0; i < strlen(magazine); i++) {
        record[magazine[i] - 'a']++;
    }
    for (int i = 0; i < strlen(ransomNote); i++) {
        if (record[ransomNote[i] - 'a'] <= 0) {
            return false;
        }else {
            record[ransomNote[i] - 'a']--;
        }
    }
    return true;
}