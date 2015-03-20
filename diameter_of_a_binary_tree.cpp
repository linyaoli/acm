/*
  The diameter of a tree (sometimes called the width) is the number
  of nodes on the longest path between two leaves in the tree. The
  diagram below shows two trees each with diameter nine, the leaves
  that form the ends of a longest path are shaded (note that there is
  more than one path in each tree of length nine, but no path longer
  than nine nodes).


  The diameter of a tree T is the largest of the following quantities:

  * the diameter of T’s left subtree
  * the diameter of T’s right subtree
  * the longest path between leaves that goes through the root of T
  (this can be computed from the heights of the subtrees of T)


  The second parameter is to store the height of tree.
   Initially, we need to pass a pointer to a location with value
   as 0. So, function should be used as follows:

   int height = 0;
   struct node *root = SomeFunctionToMakeTree();
   int diameter = diameterOpt(root, &height); */
int diameterOpt(struct node *root, int* height)
{
    /* lh --> Height of left subtree
        rh --> Height of right subtree */
    int lh = 0, rh = 0;

    /* ldiameter  --> diameter of left subtree
        rdiameter  --> Diameter of right subtree */
    int ldiameter = 0, rdiameter = 0;

    if(root == NULL)
    {
      *height = 0;
       return 0; /* diameter is also 0 */
    }

    /* Get the heights of left and right subtrees in lh and rh
      And store the returned values in ldiameter and ldiameter */
    ldiameter = diameterOpt(root->left, &lh);
    rdiameter = diameterOpt(root->right, &rh);

    /* Height of current node is max of heights of left and
       right subtrees plus 1*/
    *height = max(lh, rh) + 1;

    return max(lh + rh + 1, max(ldiameter, rdiameter));
}
