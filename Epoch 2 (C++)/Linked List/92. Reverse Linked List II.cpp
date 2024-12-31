/*
12/29/2024
Linked List
*/

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(!head || left == right) return head;

        ListNode *dummy = new ListNode(0, head);
        ListNode *pre = dummy;
        
        for(int i = 0; i < left-1 && pre->next; i++) pre = pre->next;
        
        ListNode *cur = pre->next;
        ListNode *temp = cur;

        for(int i = 0; i < right - left; i++) {
            temp = cur->next;
            cur->next = temp->next;
            temp->next = pre->next;
            pre->next = temp;
        }
        
        return dummy->next;
    }
};
