/**
 * Definition for singly-linked list.append * struct ListNode {
      *     int val;
      *     ListNode *next;
      *     ListNode(int x) : val(x), next(NULL) {}
      * };
  */
  class Solution {
      public:
          void reorderList(ListNode *head) {

                      if (head == NULL || head->next == NULL || head->next->next == NULL)
                          return;

                      ListNode *_head = head;
                      ListNode *cur = _head->next;

                      while (cur->next != NULL) {

                                      while (cur->next->next != NULL) {
                                                          cur = cur->next;
                                                      }
                                      cur->next->next = _head->next;
                                      _head->next = cur->next;
                                      _head = _head->next->next;
                                      cur->next = NULL;
                                      cur = _head->next;
                                  }
                      return;
                  }
  };
                                      }
                      }
          }
  }
 }
