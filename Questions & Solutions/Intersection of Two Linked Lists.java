/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

/*
    I calculated the lengths of both lists and
    aligned them by advancing the longer list's
    pointer by the difference. Then I traversed
    both lists together until finding the common
    node where they intersect.
    O(n + m) time O(1) space
*/

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;
        ListNode b = headB;
        int la = 0;
        int lb = 0;
        while(a != null) {
            a = a.next;
            la++;
        }
        while(b != null) {
            b = b.next;
            lb++;
        }
        if(la > lb) {
            return helper(headA, headB, la - lb);
        } else {
            return helper(headB, headA, lb - la);
        }
    }
    
    public ListNode helper(ListNode headA, ListNode headB, int diff) {
        while(diff > 0) {
            headA = headA.next;
            diff--;
        }
        
        while(headA != null && headB != null && headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
}