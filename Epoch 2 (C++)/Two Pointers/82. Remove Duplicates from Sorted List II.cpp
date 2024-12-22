/*
12/22/2024
Two Pointers
*/

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *rtn = new ListNode(0, head);
        ListNode *left = rtn;

        while(head && head->next) {
            if(head->next && head->val == head->next->val) {
                while(head->next && head->val == head->next->val) {
                    head = head->next;
                }
                left->next = head->next;
            }
            else {
                left = left->next;
            }
            head = head->next;
        }

        return rtn->next;
    }
};
