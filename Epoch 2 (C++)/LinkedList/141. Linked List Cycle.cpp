/*
11/5/2024
ListNode
*/

class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        if(!head) {
            return false;
        }

        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast && slow && fast->next) {
            if (fast == slow) {
                return true;
            }
            fast = fast->next->next;
            slow = slow->next;
        }

        return false;
    }
};
