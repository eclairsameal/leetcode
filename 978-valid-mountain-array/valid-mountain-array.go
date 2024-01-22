func validMountainArray(arr []int) bool {
    if len(arr) < 3 {
        return false;
    }
    i := 0;
    flagIncrease := false; // 上升
    flagDecrease := false; // 下降
    for ; i < len(arr)-1 && arr[i] < arr[i+1]; i++ {
        flagIncrease = true;
    }
    for ; i < len(arr)-1 && arr[i] > arr[i+1]; i++ {
        flagDecrease = true;
    }

    return i == len(arr)-1 && flagIncrease && flagDecrease; // i 有跑完整個數組且有上升跟下降 
}