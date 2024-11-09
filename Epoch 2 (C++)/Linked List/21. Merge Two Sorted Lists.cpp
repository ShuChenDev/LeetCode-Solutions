/*
11/7/2024
Linked List
*/

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {  

        
        if (!list1) {
            return list2;
        }
        if (!list2) {
            return list1;
        }

        ListNode* dummy = new ListNode();
        ListNode* rtn = dummy;
        
        while(list1 && list2) {
            if (list1->val <= list2->val) {
                dummy->next = list1;
                list1 = list1->next;                
            }
            else{
                dummy->next = list2;
                list2 = list2->next;
            }
            dummy = dummy->next;
        }

        if (list1) {
            dummy->next = list1;
        }
        else if (list2) {
            dummy->next = list2;
        }
        return rtn->next;
    }
};
