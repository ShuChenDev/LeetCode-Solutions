/*
12/5/2024
Sorting
*/

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) return head;

        ListNode* fast = head;        
        ListNode* slow = head;
        ListNode* temp = nullptr;

        while(fast && fast->next) {
            temp = slow;
            slow = slow->next;
            fast = fast->next->next;            
        }

        temp->next = nullptr;
        
        return merge(sortList(head), sortList(slow));
    }

    ListNode* merge(ListNode* left, ListNode* right) {
    
        ListNode* rtn = new ListNode();
        ListNode* cur = rtn;

        while(left && right) {
            if(left->val <= right->val) {
                cur->next = left;
                left = left->next;
            }
            else {
                cur->next = right;
                right = right->next;
            }
            cur = cur->next;
        }
                
        cur->next = left ? left : right;
        return rtn->next;
    }
};
