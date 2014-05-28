/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        while (slow && fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (slow == fast) {
                while (head != fast) {
                    head = head->next;
                    fast = fast->next;
                }
                return head;
            }

        }
        return NULL;
    }
};
