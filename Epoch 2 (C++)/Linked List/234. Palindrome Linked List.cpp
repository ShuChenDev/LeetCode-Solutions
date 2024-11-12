/*
11/12/2024
Linked List
*/

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head)
        {
            return true;
        }

        ListNode* slow = head;
        ListNode* fast = head;


        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* temp;
        ListNode* prev = NULL;
        while(slow)
        {
            temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        } 

        ListNode* left = head;
        ListNode* right= prev;

        while(right)
        {
            if(left->val != right->val)
            {
                return false;
            }
            left = left->next;
            right = right->next;
        }
        return true;


    }
};
