func numberOfSteps(num int) int {
    n := 0
    for num > 0 {
        if num % 2 == 0 {
            num = int(num/2);
        } else {
            num -= 1;
        }
        n++;
    }
    return n
}