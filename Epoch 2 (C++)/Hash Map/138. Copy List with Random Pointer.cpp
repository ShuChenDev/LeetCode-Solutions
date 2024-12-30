/*
12/30/2024
Hash Map
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> map;
        Node* dummy = head;
        
        while(dummy) {
            map[dummy] = new Node(dummy->val);
            dummy = dummy->next;
        }
        
        dummy = head;
        
        while(dummy) {
            map[dummy]->next = map[dummy->next];
            map[dummy]->random = map[dummy->random];
            dummy = dummy->next;
        }

        return map[head];
    }
};
