/**
 *  given: L0->L1->L2->L3.....->Ln
 *  return: L0->Ln->L1->Ln-1->L2.....
 *
 */

LinkedList* lst = head;
LinkedList* mid; // we can find the mid node, using head->next and head->next->next.
void reorder(LinkedList* head) {
    if(!head) return;
    if(lst == mid) return;
    reorder(head->next);
    head->next = lst->next;
    lst->next = head;
    lst = head->next;
}
