
#include <stdio.h>
#include <stdlib.h>

typedef struct LinkedList{
    struct LinkedList* next;
    int val;
}LNode;

int del(LNode* q, int n){

    LNode* dummy = (LNode*)malloc(sizeof(LNode));
    dummy->val = -1;
    dummy->next = q;
    LNode* p = dummy;
    while (q != NULL) {
      if (q->val == n) {
        p->next = p->next->next;
        free(q);
        q = p->next;
      }
      else{
        p = p->next;
        q = q->next;
      }
    }

    q = dummy->next;
    while (q!=NULL){
      printf("%d ", q->val);
      q = q->next;
    }
    return -1;
}

int main(void) {

    LNode* lst = (LNode*)malloc(sizeof(LNode));
    LNode* start = lst;
    int i = 0;
    int a[10] = {1,2,1,2,3,4,5,6,7,6};
    for (i=0;i<10;i++) {
        LNode* newNode = (LNode*)malloc(sizeof(LNode));
        newNode->val = a[i];
        start->next = newNode;
        start = newNode;
    }
    start->next = NULL;
    start = lst;
//    while (start != NULL)
//    {
//      printf("%d ", start->val);
//      start = start->next;
//    }
    del(lst, 7);

    return 0;
}

void removeNode(int val, LinkedList **list) {
     LinkedList *prev = *list;
     while (prev && prev->val == val)
          prev = prev->next;

     *list = prev;

      if (*list == NULL)
           return;

      LinkedList *next = prev->next;

      while (next) {
          if (next->val == val)
              prev->next = next->next;
          else
              prev = next;

          next = next->next;
      }
}

void removeNode(int val, ListNode **list) {
    while(*list!=NULL){
        if((*list)->val==val){
        ListNode *next=(*list)->next;
        free( *list);
        *list=next;
        }
        else {
            list=&(*list)->next;
        }
    }
}
