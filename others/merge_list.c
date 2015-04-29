#include <stdlib.h>

ListNode* sortList(ListNode* head) {
    if (head == NULL) return NULL;
    int len = 0;
    ListNode* it = head;
    while(it) {
        len ++;
        it = it->next;
    }
    ListNode* newHead = sort(&head, len);
    return newHead;
}

ListNode* sort(ListNode** head, int length) {
    if (length == 1) {
        ListNode* temp = *head;
        *head = (*head)->next;
        temp->next = NULL;
        return temp;
    }
    ListNode* leftHead = sort(head, length/2);
    ListNode* rightHead = sort(head, length - length/2);
    ListNode* newHead = Merge(leftHead, rightHead);
    return newHead;
}

ListNode* merge(ListNode* first, ListNode* second) {
    ListNode* head = new ListNode(-1);
    ListNode* cur = head;
    while(first != NULL || second != NULL) {
        int fv = first == NULL ? INT_MAX:first->val;
        int sv = second == NULL ? INT_MAX:second->val;
        if (fv <= sv) {
            cur->next = first;
            first = first->next;
        }
        else {
            cur->next = second;
            second = second->next;
        }
        cur = cur->next;
    }
    cur = head->next;
    delete head;
    return cur;
}
