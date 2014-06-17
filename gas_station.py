class Solution:
    def canCompleteCircuit(self, gas, cost):
        sum = _sum = start = 0
        for i in range(0, len(gas), 1):
            sum += gas[i] - cost[i]
            _sum += gas[i] - cost[i]
            if sum < 0:
                sum = 0
                start = i + 1

        if _sum < 0:
            return -1
        return start
