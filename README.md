Code Test
===============
 Code test on tons of simple algorithm questions.

|    No.    |  Challenge Name  |     Tag       |            Description                 |
|-----------|------------------|---------------|----------------------------------------|
|    0      |  single number   |  bitwise      | find num appears only once.            |
|    1      |  single number ii|  bitwise      | find num appears once while others 3s. |
|    2      |  3 sum           |  sort, hash   | pick 3 nums : x + y + z = target.      |
|    3      |  3 sum closest   |  sort, hash   | pick 3 sums to min abs(target-(x+y+z)).|
|    4      |  4 sum           |  sort, hash   | pick 4 nums: x + y + z + d = target.   |
|    5      |  tree preorder   |  tree         | preorder traversal of bianry tree.     |
|    6      |  LRU cache       |  hash         | implement a LRU cache.                 |
|    7      |  add binary      |  bitwise      | add two binaries.                      |
|    8      |  add 2 numbers   |  string       | add two numbers.                       |
|    9      |  anagrams        |  hash         | group anagrams.                        |
|    10     |  atoi            |  string       | string to integer.                     |
|    11     |  combination sum |  backtrack    |  find sum of several nums = target   |
|12|jump game | dynamic | determine if can reach the end.|
|13|spiral matrix| recursion | convert matrix to spiral order.|
|14|maximum subarray| dynamic | maximum sum of contiguous subarray. |
|15|combination sum ii| backtrack, hash | similar to 11, avoid duplicates.|
|16|multiply strings|string | return multiplication of the numbers as a string.|
|17|pow(x,n)|divide & conquer|
|18|permutations|backtrack|return all permutations|
|19|rotate image|array | rotate matrix by 90 degrees.(clockwise, inplace)|
|20|2 sum| sort, hash | find x + y = target, return index|
|21|permutations ii| backtrack & visited|avoid duplicates|
|22|balanced binary tree| tree| balanced?|
|23|best time stock | dynamic | track the minimum price and find the largest difference |
|24|best time stock ii | dynamic| key:: stock[i+n] - stock[i]  = stock[i+n] - stock[i+n-k] + stock[i+n-k] - stock[i]|
|25|betting result|||
|26|binary search| divide&conquer||
|27|BST iterator|tree||
|28|tree inorder traversal|tree||
|29|wildcard matching| string | pattern matching of '?' and * |
|30|n queens|backtrack | find all valid sol in NxN board.|
|31|trapping rain water| dynamic | find left highest and right highest for each vol.|
|32|first missing positive| partition | O(n) time, O(1) space, |
|33|n queens ii | backtrack|count valids|
|34|merge intervals| dynamic| |
|35|insert intervals| dynamic| |
|36|sudoku solver|backtrack| disgusting problem, use solution of valid sudoku|
|37|valid number| string | many cases to consider|
|38|edit distance | dynamic | insert, del, replace a char each distance, related to No.40|
|39|search in rotated sorted array | divide & conquer| careful with cases|
|40|minimum window substring| dynamic | two pointers, s[slow:fast] always have all the chars needed.|
|41|longest valid parentheses | dynamic||
|42|candy | dynamic adjustment | adjust the candies whenever there is a trough |
|43|dungeon game |dynamic  | table filling|
|44|word break| backtrack & optimization | cut off unnecessary leafs|
|45|valid parentheses | stack & string | |
|46|merge sorted array| linear time | tail -> head merge|
|47|excel sheet column number|
|48|intersection of two linked lists|O(n) time O(1) space|
|49|zigzag conversion | O(n) time math solution | dont touch this question!|
|50|min stack| stack |retrive by maintaining another stack for mins|
|51|reverse integer| careful with overflow||
|52|string to integer|careful with white spaces, -/+ ,  illegal chars and overflow||
|53|palindrome number | O(1) space -> do not use recursion (use stack space, which is not constant)||
|54|roman to integer | (／‵Д′)／~ ╧╧ |
|55|longest common prefix|string |
|56|remove nth node from end of the list| linkedlist | fast and slow pointer|
|57|pascal triangle ii | pure math problem c30, c31, c32, c33, be aware of the ultimate optimization.|
|58|pascal triangle | read 57.||
|59|factorial trailing zeroes | find all those 5s||
|60|path sum | tree, recursion||
|61|minimum depth tree| tree, recursion||
|62|binary tree level order traversal ii| queue ||
|63|maximum depth of binary tree| recursion, make it concise||
|64|binary tree level order traversal | queue||
|65|symmetric tree|recursion|recursion| check(node1.left, node2.right)&&check(node1.right, node2.left)|
|66|same tree | recursion | isSameTree(p.left, q.left)&&isSameTree(p.right, q.right)|
|67|remove duplicates from sorted array| two pointer ||
|68|merge sorted array|from end to start, use empty space||
|69|remove element|two pointers||
|70|implement strStr()| brute O(m*n), optimized KMP solution O(m+n)||
|71|remove duplicates from sorted list|O(n)||
|72|climb chairs| dynamic ||
|73|plus one| |||
|74|valid soduku|check every row, column and 3x3 boxes.||
|75|add binary|string||
|76|merge two sorted lists|linked list, basic op of merge sort, either merge two into one and splice ont to another||
|77|length of last word|return the length of last word of a string.|make it as neat as possible.|
|78|gray code|find the patterns lie within the sequence||
|79|find peak element| binary search | O(logn)|
|80|gas station|dynamic | maintain a sum var, if it becomes negative, which means current start is not valid, start a new route in the next station.|
|81|clone graph| queue, graph, breath-first traversal| use nodeMap to mark the connectivity between graph node and cloned node|
|82|palindrome partitioning| backtrack | cutoff unnecessary branches.|
|83|surrounded regions| mark 0s on the edge, then find those 0s connected to them.||
|84|sum root to leaf|recursion| path = path*10 + root.val|
|85|3sum closest|similar to 3sum||
|86|4sum | preprocess the sum of all pais and store in dict for lookup can reduce time cost||
|87|word ladder|graph| do it either dfs or iteratively bfs||
|88|letter combinations of a phone number|backtrack|make a dict of num -> letters|
|89|longest substring without repeating characters|dynamic| map or a lookup table, make it neat|
|90|triangle| dynamic | similar to finding num of path in grid|
|91|longest palindrome substring| common O(n*n) with optimization| Manacher's method, linear solution|
|92|binary search tree iterator| recursion | make it neat|
|93|repeated DNA sequence|ez, use map|
|94|largest number| compare : int(str(s2) + str(s1)) - int(str(s1) + str(s2)) ||
|95|populating next right pointers in each node|recursion, use the transitivity|
|96|generate parenthesis|backtrack, track left_num and right_num||
|97|flatten binary tree to linkedlist|bottom-up||
|98|path sum ii|recursion, top-down||
|99|convert sorted array to binary search tree|recursion|inorder, topdown|
|100|convert sorted list to binary search tree|recursion |similar to 99|
|101|construct binary tree from inorder and postorder traversal|recursion||
|102|construct binary tree from preorder and inorder traversal|recursion||
|103|find minimum in rotated sorted array|ans = min(ans, num[mid])||
|104|binary tree zigzag order traversal|queue, track the level order||
|105|maximum product subarray|dynamic| track the minimum value in case of negative|
|106|reverse words in a string|||
|107|evaluate reverse polish notation|stack| make it neat.|
|108|swap nodes in pairs|linked list| do it in space|p, q, r three pointers, p is the node before two swapped nodes.|
|109|validate binary search tree|track the min and max of each path, top-down||











=======


Limitations
-----------


Feature ideas
-------------
![Alt text](/tree.png)

Contributing code
-----------------
feel free to use and contribute.

Donations
---------

Disclaimer
----------
Most of the questions are from leetcode, CTCI and geeks4geeks.
