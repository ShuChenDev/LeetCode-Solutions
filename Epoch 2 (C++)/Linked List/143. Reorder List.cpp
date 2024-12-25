/*
12/25/2024
ListNode
*/

class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head) return;

        ListNode *dummy = head;
        ListNode *mid = head;
        ListNode *temp = head;

        while(temp->next && temp->next->next) {
            mid = mid->next;
            temp = temp->next->next;
        }
        if(temp->next) mid = mid->next;

        ListNode *pre = NULL;
        while(mid) {
            temp = mid->next;
            mid->next = pre;
            pre = mid;
            mid = temp;
        }
        mid = pre;

        while(dummy && mid) {
            temp = dummy->next;
            pre = mid->next;
            dummy->next = mid;
            mid->next = temp;
            dummy = temp;
            mid = pre;
        }
        if (dummy && dummy->next) dummy->next = NULL;
    }
};
