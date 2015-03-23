"""
/* initialization */
pCrawl = root
set initial stack element as NULL (sentinal)

/* traverse upto left extreme */
while(pCrawl is valid )
   stack.push(pCrawl)
   pCrawl = pCrawl.left

/* process other nodes */
while( pCrawl = stack.pop() is valid )
   stop if sufficient number of elements are popped.
   if( pCrawl.right is valid )
      pCrawl = pCrawl.right
      while( pCrawl is valid )
         stack.push(pCrawl)
         pCrawl = pCrawl.left
"""
"""
The idea is to maintain rank of each node. We can keep track of elements in a subtree
of any node while building the tree. Since we need K-th smallest element, we can maintain
number of elements of left subtree in every node.

Assume that the root is having N nodes in its left subtree. If K = N + 1, root is K-th node.
If K < N, we will continue our search (recursion) for the Kth smallest element in the left subtree of root.
If K > N + 1, we continue our search in the right subtree for the (K – N – 1)-th smallest element.
Note that we need the count of elements in left subtree only.

O(height)
"""

start:
if K = root.leftElement + 1
   root node is the K th node.
   goto stop
else if K > root.leftElements
   K = K - (root.leftElements + 1)
   root = root.right
   goto start
else
   root = root.left
   goto srart

stop:
