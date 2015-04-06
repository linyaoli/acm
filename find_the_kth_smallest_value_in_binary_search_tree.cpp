#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *left, *right;
};

struct node* newNode(int data)
{
	struct node *tmp = (struct node*)malloc(sizeof(struct node));
	tmp->data = data;
	tmp->left = tmp->right = NULL;
	return tmp;
}

int countNodes(struct node *root)
{
	if(!root)
		return 0;

	return (countNodes(root->left) + 1 + countNodes(root->right));
}

struct node* KthSmallestNode(struct node *root, int k)
{
	int lcount;

	if(!root)
		return NULL;
	lcount = countNodes(root->left);
	if(lcount == k - 1)
		return root;
	else if(lcount > k - 1)
		return KthSmallestNode(root->left, k);
	else
		return KthSmallestNode(root->right, k - (lcount + 1));
}


int main()
{
	struct node *KthNode = NULL;
	struct node *t = newNode(20);
	t->left = newNode(8);
	t->left->left = newNode(4);
	t->left->right = newNode(12);
	t->right = newNode(22);
	t->left->right->left = newNode(10);
	t->left->right->right = newNode(14);

	KthNode = KthSmallestNode(t, 3);
	if(KthNode)
		printf("%d\n", KthNode->data);
	else
		printf("Not Found!\n");

}
