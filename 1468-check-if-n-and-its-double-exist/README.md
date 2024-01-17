<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">Check If N and Its Double Exist</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that :</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>


## 說明：
arr 陣列裡有存在 arr 陣列裡某個值的倍數值嗎。

## 解決方案：python - in
* 注意：關於0要特別處裡
```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for n in arr:
            if n*2 in arr and n != 0: 
                return True
            elif arr.count(0) >= 2: # [0,0,0,0] 
          # elif arr.count(0) == 2: # [0,0,0,0] -> error
                return True
        return False
```
### 解決方案：hash table - set  
我們也可以使用hash table資料結構使用 Set 物件或陣列來解決這個問題。

1. 迭代數組並檢查數組中的元素乘以 2 或除以 2 是否等於物件中的元素Set。
2. 如果存在則回傳true
3. 如果不存在，則將該元素新增至 Set 物件。
