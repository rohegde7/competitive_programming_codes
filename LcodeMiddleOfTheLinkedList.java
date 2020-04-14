/*

https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/529/week-2/3290/

Author:
Rohit Hegde
github.com/rohegde7
hegde.rohit7@gmail.com

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.


/*

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


class Solution {
    
    public ListNode middleNode(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode pointer1 = head;
        ListNode pointer2 = head.next;
        
        while (pointer2 != null) {
        
            pointer2 = pointer2.next;   
         	if (pointer2 != null)
            	pointer2 = pointer2.next;
            
            ointer1 = pointer1.next;
        }
        
        return pointer1;
    }
}