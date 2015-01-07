+----------------------------------------+
Number of nodes in the tree.
+----------------------------------------+
Recursively:
def getNodeNumRec(self, root):
    if not root:
        return 0
    return 1 + self.getNodeNumRec(root.left) + self.getNodeNumRec(root.right)

Iteratively:
def getNodeNum(self, root):
    if not root:
        return 0
    stack = []
    stack.append(root)
    count = 0
    while stack != []:
        node = stack.pop()
        node += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return count
+----------------------------------------+
Depth of binary tree.
+----------------------------------------+
Recursively:
def getDepthRec(self, root):
    if not root:
        return 0
    return 1 + max(self.getDepthRec(root.left), self.getDepthRec(root.right))

+----------------------------------------+
Traversal.
+----------------------------------------+
def postorderTraversal(self, root):
    if not root:
        return None
    self.postorderTraversal(root.left)
    self.postorderTraversal(root.right)
    print root

+----------------------------------------+
Level order traversal.
+----------------------------------------+
def levelTraversal(self, root):
    if not root:
        return None
    queue = []
    queue.append(root)
    while queue != []:
        node = queue.pop(0)
        print node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

Recursively?

def printLevel(self, root):
    h = self.height(root)
    for i in xrange(1, h + 1):
        self.printlvl(root, i)

def printlvl(self, root, lvl):
    if not root:
        return
    if lvl == 1:
        print root.val
    else:
        printlvl(root.left, lvl - 1)
        printlvl(root.right, lvl - 1)

def height(self, root):
    if not root:
        return 0
    else:
        l_h = self.height(root.left)
        r_h = self.height(root.right)
        return 1 + max(l_h, r_h)

+----------------------------------------+
Convert BST to sorted double linked list.
+----------------------------------------+
Recursively:
def convertBST2DLLRec(self, root):
    if not root:
        return None
    l_child = self.convertBST2DLLRec(root.left)
    r_child = self.convertBST2DLLRec(root.right)
    if l_child:
        l_child.right = root
        root.left = l_child
    if r_child:
        r_child.left = root
        root.right = r_child

    if not r_child:
        return root
    else:
        return r_child

+----------------------------------------+
Get the number of nodes in level N.
+----------------------------------------+
Recursively:
def getNum(self, root, N):
    return self.gen(root, N, 1)

def gen(self, root, N, level):
    if not root:
        return 0
    if level == N:
        return 1
    return self.gen(root.left, N, level + 1) + self.gen(root.right, N, level + 1)

+----------------------------------------+
Get the number of leaf nodes.
+----------------------------------------+
Recursively:

def getNum(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    return self.getNum(root.left) + self.getNum(root.right)

+----------------------------------------+
Check if two trees are the same.
+----------------------------------------+
Recursively:

def check(self, rootA, rootB):
    if not rootA and not rootB:
        return True
    elif not rootA or not rootB:
        return False
    elif rootA.val != rootB.val:
        return False
    else:
        return self.check(rootA.left, rootB.left) and \
            self.check(rootA.right, rootB.right)

+----------------------------------------+
Check if one tree is a mirror of another.
+----------------------------------------+

def check(self, rootA, rootB):
    if not rootA and not rootB:
        return True
    elif not rootA or not rootB:
        return False
    elif rootA.val != rootB.val:
        return False
    else:
        return self.check(rootA.left, rootB.right) and \
            self.check(rootA.right, rootB.left)

+----------------------------------------+
Lowest Common Ancestor.
+----------------------------------------+

def findLCA(self, root, nodeA, nodeB):
    if not root:
        return False
    if root == nodeA or root == nodeB:
        return True

    l_h = self.findLCA(root.left, nodeA, nodeB)
    r_h = self.findLCA(root.right, nodeA, nodeB)
    if l_h and r_h:
        #LCA found.
        return node
    else:
        return l_h or r_h

+----------------------------------------+
Get max distance between two nodes in tree.
+----------------------------------------+

self.dist = 0
def maxDist(self, root):
    if not root:
        return
    if not root.left:
        root.maxleft = 0
    else:
        self.maxDist(root.left)

    if not root.right:
        root.maxright = 0
    else:
        self.maxDist(root.right)

    if root.left:
        tmpMax = 0
        if root.left.maxleft > root.left.maxright:
            tmpMax = root.left.maxleft
        else:
            tmpMax = root.left.maxright
        root.maxleft = tmpMax + 1

    if root.right:
        tmpMax = 0
        if root.right.maxleft > root.right.maxright:
            tmpMax = root.right.maxleft
        else:
            tmpMax = root.right.maxright
        root.maxright = tmpMax + 1

    if root.maxleft + root.maxright > self.dist:
        self.dist = root.maxleft + root.maxright

+----------------------------------------+
Rebuild tree from preorder and inorder.
+----------------------------------------+



+----------------------------------------+
Check if the tree is complete.
+----------------------------------------+
def checkComplete(self, root):
    if not root:
        return True
    flag = False
    queue = [root]
    while queue != []:
        node = queue.pop(0)
        if node.left:
            if flag:
                return False
            queue.append(node.left)
        else:
            flag = True

        if node.right:
            if flag:
                return False
            queue.append(node.right)
        else:
            flag = True

    return True

+----------------------------------------+
Find the longest sub bunch.
i.e. continuous nodes all to the left / right.
+----------------------------------------+
