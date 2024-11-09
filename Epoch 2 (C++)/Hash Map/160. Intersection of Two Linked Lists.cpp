/*
11/9/2024
Hash Map
*/

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        unordered_map<ListNode*, int> visited;

        while(headA && headB) {
            visited[headA]++;
            headA = headA->next;
        }

        while(headB) {
            if(visited[headB]){
                return headB;
            }
            headB = headB->next;
        }
        
        return NULL;
    }
};
