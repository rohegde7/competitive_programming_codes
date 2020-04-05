/*

https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/

Author:
Rohit Hegde
github.com/rohegde7
hegde.rohit7@gmail.com

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

*/

import java.util.HashSet;
import java.util.Set;

class Solution {

    public static void main(String[] args) {
        System.out.println(isHappy(21));
    }


    public static boolean isHappy(int number) {

        Set<Integer> numberSumSet = new HashSet<>();

        while (number != 1) {
            String[] numberArray = String.valueOf(number).split("");

            int sumOfSquares = 0;

            for (int i = 0; i < numberArray.length; i++) {
                int currentElement = Integer.parseInt(numberArray[i]);
                sumOfSquares += currentElement * currentElement;
            }

            boolean additionSuccessful = numberSumSet.add(sumOfSquares);

            if(!additionSuccessful) return false;

            number = sumOfSquares;
        }

        return true;
    }
}