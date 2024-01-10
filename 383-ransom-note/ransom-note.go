func canConstruct(ransomNote string, magazine string) bool {
    if (len(magazine) < len(ransomNote)) {
        return false
    }
    record := make([]int, 26)
    for _, c := range magazine {
        record[c - 'a']++
    }
    for _, c := range ransomNote {
        if record[c - 'a'] <= 0 {
            return false
        } else {
            record[c - 'a']-=1
        }
    }
    return true
}