func maximumWealth(accounts [][]int) int {
    max_money := 0
    for i, account := range accounts {
        sum := 0
        for _, money := range account {
            sum += money
        }
        if i == 0 || max_money < sum{
            max_money = sum
        }
    }
    return max_money
}