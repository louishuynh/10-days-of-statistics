Interquartile Range
====================

Task
-----
The interquartile range of an array is the difference between its first (Q_1) and third (Q_3) quartiles (i.e., Q_3-Q_1).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, 
construct a data set, S, where each x_i occurs at frequency f_i. 
Then calculate and print S''s interquartile range, rounded to a scale of  decimal place (i.e., 12.3 format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set 
with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format
-------------
The first line contains an integer, , denoting the number of elements in arrays  and . 
The second line contains  space-separated integers describing the respective elements of array . 
The third line contains  space-separated integers describing the respective elements of array .

Constraints
------------

5 <= n <= 50
0 <= x_i <= 100, where x_i is the ith element of array X.
0 < sum i=0 to n-1 f_i <= 10*3, where f_i is the ith element of array F
The number of elements in S is equal to Sum F.

Output Format
--------------
Print the interquartile range for the expanded data set on a new line. 
Round your answer to a scale of  decimal place (i.e., format).