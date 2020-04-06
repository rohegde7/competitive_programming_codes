/*

https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3286/

Author:
Rohit Hegde
github.com/rohegde7
hegde.rohit7@gmail.com

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

*/

class Solution {

    public static void main(String[] args) {

        int arr[] = {0, 1, 0, 3, 12};

        printArray(arr);

        moveZeroes(arr);

        printArray(arr);
    }


    public static void moveZeroes(int[] nums) {

        int pointer1 = 0;
        int pointer2 = 1;

        while (pointer1 < nums.length) {

            while (pointer1 < nums.length && nums[pointer1] != 0)
                pointer1++;

            if (pointer1 >= nums.length - 1) return;

            pointer2 = pointer1 + 1;

            while (pointer2 < nums.length - 1 && nums[pointer2] == 0)
                pointer2++;

            if (pointer2 > nums.length - 1) return;

            int temp = nums[pointer1];
            nums[pointer1] = nums[pointer2];
            nums[pointer2] = temp;

            pointer1++;
            pointer2++;
        }
    }

    public static void printArray(int arr[]) {

        for (int i = 0; i < arr.length; i++) {

            System.out.print(arr[i] + " ");
        }

        System.out.println();
    }
}