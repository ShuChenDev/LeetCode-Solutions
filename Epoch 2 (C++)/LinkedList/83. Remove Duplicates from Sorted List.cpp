/*
11/8/2024
Linked List
*/

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) {
            return head;
        }

        ListNode* dummy = head;

        while(dummy->next) {
            if(dummy->val == dummy->next->val) {
                if(dummy->next->next) {
                    dummy->next = dummy->next->next;
                }
                else {
                    dummy->next = NULL;
                    return head;
                }
            }
            else {
                dummy = dummy->next;
            }
        }
        return head;
    }
};
