/*
12/20/2024
Linked List
*/

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {

        if(!head || !head->next) return head;
        ListNode *dummy = head;
        int len = 1;
    
        while(dummy->next) {
            dummy = dummy->next;
            len++;
        }

        k = k % len;

        dummy = head;
        ListNode *cur = dummy;
        
        for(int i = 0; i < k; i++) {
            dummy = head;
            cur = dummy;
            
            while(dummy->next) {
                cur = dummy;
                dummy = dummy->next;
            }

            cur->next = nullptr;
            dummy->next = head;
            head = dummy;
        }
        
        return head;
    }
};
