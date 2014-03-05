#include <stdio.h>
#include <stdlib.h>

struct LinkedList {
    struct LinkedList* next;
    int value;
}*start;

typedef struct LList {
    struct LList* next;
    int value;
}Node, *LNode;

void split(struct LinkedList* start) {

    int i = 0;

    //Node* n = (Node*)malloc(sizeof(Node));
    LNode*n = (LNode*)malloc(sizeof(Node));
    while(start->next != NULL) {

        if (i%2==0) {
            printf("list1:%d \n", start->value);
        }
        else {
            printf("list2:%d \n", start->value);
        }
        i++;

        start = start->next;
    }
}

int main (void) {
    int i = 0, n = 10;
    struct LinkedList* original, *now;
    original = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    start = original;
    now = start;
    original->value = 1;
    for (i = 1; i < n; i++){
        struct LinkedList* newNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
        newNode->value = i;
        now->next = newNode;
        now = newNode;
    }

    split(start);

    return 0;
}



