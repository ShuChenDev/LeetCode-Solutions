/*
11/27/2024
Hash Map
*/

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> set;
        if(!head) {
            return head;
        }

        while(head->next) {
            if(set.find(head) != set.end()) {
                return head;
            } 
            set.insert(head);
            head = head->next;
        }

        return NULL;
        
    }
};
