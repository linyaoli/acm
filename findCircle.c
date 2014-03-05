#include <stdio.h>
#include <stdlib.h>

typedef struct LinkedList{
    struct LinkedList* next;
}LNode;

int findCircle(LNode* in){

    LNode* fast = in->next->next;
    LNode* slow = in;
    int i=0;
    while (fast != slow) {
        fast = fast->next->next;
        slow = slow->next;
        i++;
        printf("%d\n", i);
    }
    printf("find circle!");
    return 1;
}

int main(void) {

    LNode* lst = (LNode*)malloc(sizeof(LNode));
    LNode* start = lst;
    int i = 0;
    for (i=0;i<10;i++) {
        LNode* newNode = (LNode*)malloc(sizeof(LNode));
        start->next = newNode;
        start = newNode;
    }
    start->next = lst->next->next->next->next;
    findCircle(lst);
    return 0;
}
