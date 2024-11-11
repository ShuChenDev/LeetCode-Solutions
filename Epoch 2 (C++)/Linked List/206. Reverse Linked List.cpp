/*
11/11/2024
Linked List
*/

class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        if(!head)
        {
            return head;
        }

        ListNode* temp = new ListNode();
        ListNode* prev = NULL;
        

        while(head)
        {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;        
        }
        return prev;
    }
};
