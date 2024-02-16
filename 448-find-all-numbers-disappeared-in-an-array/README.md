<h2><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array">Find All Numbers Disappeared in an Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>


## 解題

題目要求不能用多的空間，所以只能利用現有數組的空間，正負號剛好可以用來代表存在跟不存在，所以當遊歷數組時，數組裡數字對應的index的值標記為負數。
最後再回傳數組中為正數的index+1的值，就可以知道哪些數字沒出現過。

## 參考
https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0448.Find%20All%20Numbers%20Disappeared%20in%20an%20Array
