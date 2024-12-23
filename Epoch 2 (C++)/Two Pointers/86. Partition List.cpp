/*
12/23/2024
Two Pointers
*/

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if(!head) return head;

        ListNode *left = new ListNode();
        ListNode *right = new ListNode();
        ListNode *leftdummy = left;
        ListNode *rightdummy = right;
        
        while(head) {                
            if(head->val < x) {
                left->next = head; left = left->next;
            }
            else {
                right->next = head;
                right = right->next;
            } 
            head = head->next;
        }
        left->next = rightdummy->next;
        right->next = NULL;

        return leftdummy->next;
    }
};
