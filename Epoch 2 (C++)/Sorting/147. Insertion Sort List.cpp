/*
12/4/2023
Sort & Linked List
*/

class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        
        ListNode* dummy = new ListNode(0);
        dummy -> next = head;
        ListNode* cur = head;

        while(cur) {
            if(cur->next && cur->next->val < cur->val) {
                ListNode* temp = dummy;
                while(temp->next && temp->next->val < cur->next->val) {
                    temp = temp->next;
                }

                ListNode* temp2 = temp->next;                
                temp->next = cur->next;
                cur->next = cur->next->next;
                temp->next->next = temp2;
            }
            else {
                cur = cur->next;
            }
        }

        return dummy->next;;
    }
};
