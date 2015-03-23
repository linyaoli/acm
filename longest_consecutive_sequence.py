"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        """
        lookup = {}
        for i in num:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        cons = 1
        max = 1
        lookup = sorted(lookup)
        print lookup
        for i in xrange(1, len(lookup)):
            if lookup[i] - lookup[i-1] == 1:
                cons += 1
                if cons > max:
                  max = cons
            else:
                cons = 1
        return max
        """

#你看到[100, 4, 200, 1, 3, 2]这个数组，首先你会看99或者101在不在这个数组里，发现数组没这两个数，那么100组成的连续序列长度仅为1。接着会看5或者3在不在数组里，会发现3存在，5不存在；紧接着会看2在不在....直到发现0不在。从而得到4组成的最长序列为4。


public class Solution {
    public int longestConsecutive(int[] num) {
        Set<Integer> set = new HashSet<Integer>();
		int max = 1;
		for (int e : num)
			set.add(e);
		for (int e : num) {
			int left = e - 1;
			int right = e + 1;
			int count = 1;
			while (set.contains(left)) {
				count++;
				set.remove(left);
				left--;
			}
			while (set.contains(right)) {
				count++;
				set.remove(right);
				right++;
			}
			max = Math.max(count, max);
		}
		return max;
    }
}

sol = Solution()
print sol.longestConsecutive([100,4,200,1,3,2])
