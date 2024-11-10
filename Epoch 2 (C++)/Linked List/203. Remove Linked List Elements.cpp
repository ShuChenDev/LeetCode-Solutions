/*
11/10/2024
Linked List
*/

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(!head) 
        {
            return head;
        }
        
        head = new ListNode(0, head);
        ListNode* dummy = head;

        while(dummy) 
        {
            if(dummy->next && dummy->next->val == val) 
            {
                if(dummy->next->next) 
                {
                    dummy->next = dummy->next->next;
                }
                else 
                {
                    dummy->next = NULL;
                    break;
                }
            }
            else if(dummy->next) 
            {
                dummy = dummy->next;
            }
            else
            {
                break;
            }
        }
        return head->next;
    }
};
