<h2><a href="https://leetcode.com/problems/valid-mountain-array">Valid Mountain Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>arr</code>, return <em><code>true</code> if and only if it is a valid mountain array</em>.</p>

<p>Recall that arr is a mountain array if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i] </code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>
<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [2,1]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [3,5,5]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [0,3,2,1]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>

## 說明：

判斷一個整數的數組 arr 是不是有效的山脈數組。

## 解題 - 雙指針：

左邊到山峰跟山峰到右邊都要是遞增的。

可以使用兩個指標 left 跟 right 依照下面的規則移動：
```
arr[left] < arr[left +1] -->  left向右移動：left +1
arr[right] < arr[right -1] -->  right向左移動：right -1
```
當指標 left 跟 right 在中間相遇的話，說明此地為山峰。

注意：
* 當 left 或 right 沒有移動的話，說明是一個單調遞增或遞減的數組，依然不是山峰。
* 因為 left 和 right 是數組邊界，移動的過程中註意不要越界。

## 解題 - 單一指針：

判斷此數組 arr 是否有上坡跟下坡

走訪  arr 數組，並用 2 個flag來記錄是否有上坡跟下坡
```
flagIncrease = false // 上升
flagDecrease = false // 下降
```
當同時有上坡跟下坡且迴圈有執行到最後的話( i = len(arr)-1)，是有效的山脈數組。
