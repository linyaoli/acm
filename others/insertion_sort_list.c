ListNode* sortList(ListNode* head) {
    if(head == NULL) return NULL;
    int len = 0;
    ListNode* sort_1 = head;
    ListNode* sort_2 = head->next;
    while(sort_1) {
        while(sort_2) {

            if (sort_1->val > sort_2->val)
                insert(sort_2, sort_1);
            sort_2 = sort_2->next;
        }
        sort_1 = sort_1->next;
    }
}
//not fully finished, just the principal.

ListNode* insert(ListNode* src, ListNode* pos) {

    src->next = pos->next;
    pos->next = src;
    return pos;

}
