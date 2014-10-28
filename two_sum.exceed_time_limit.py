class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index_num = dict()
        count_num = dict()
        for i in xrange(len(num)):
            if num[i] not in index_num.keys():
                index_num[num[i]] = [i + 1]
            else:
                index_num[num[i]].append(i + 1)

            if num[i] not in count_num:
                count_num[num[i]] = 1
            else:
                count_num[num[i]] += 1

        for i in index_num.keys():
            if i * 2 == target:
                # check two same num
                if count_num[i] >= 2:
                    return (index_num[i][0], index_num[i][1])
            if i <= target and (target - i in index_num.keys()):
                return (index_num[i][0], index_num[target-i][0])
