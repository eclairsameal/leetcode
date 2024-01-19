func replaceElements(arr []int) []int {
    i := len(arr)-2
    r := arr[len(arr)-1]
    temp := 0
    for i >= 0 {
        temp = arr[i]
        arr[i] = r
        r = max(temp, r)
        i--
    }
    arr[len(arr)-1] = -1
    return arr
}