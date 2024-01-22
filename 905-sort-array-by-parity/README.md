<h2><a href="https://leetcode.com/problems/sort-array-by-parity">Sort Array By Parity</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code>, move all the even integers at the beginning of the array followed by all the odd integers.</p>

<p>Return <em><strong>any array</strong> that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,2,4]
<strong>Output:</strong> [2,4,3,1]
<strong>Explanation:</strong> The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
</ul>

## 題目大意:
給定一個整數數組 nums，移動數組所有的偶數到數組的頭，然後移動所有奇數到數組的尾。

## 解題思路：

用 2 個指標 forward 跟 after 指向頭跟尾。

當 forward 等於奇數同時 after等於偶數時交換數值。

當 forward 等於偶數時 forward 加一。

當 after 等於奇數時 after 減一。

停止條件： forward >= after時
