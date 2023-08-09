# 1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at </br>
different altitudes. The biker starts his trip on point 0 with altitude equal 0. </br>

You are given an integer array gain of length n where gain[i] is the net gain </br>
in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). </br>
Return the highest altitude of a point. </br>

## Example 1:

Input: gain = [-5,1,5,0,-7] </br>
Output: 1 </br>
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1. </br>

## Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2] </br>
Output: 0 </br>
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0. </br>

## Constraints:

n == gain.length </br>
1 <= n <= 100 </br>
-100 <= gain[i] <= 100 </br>
