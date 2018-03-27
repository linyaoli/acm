#given a stream of numbers, track the median number.
import heapq as hq
#python does not support max heap, so the following code
#is not runnable.
maxheap = []
minheap = []

def addNum(num):
    if len(maxheap) == len(minheap):
        if len(minheap) != 0:
            maxheap.heappush(minheap.pop())
            minheap.heappush(num)
        else:
            maxheap.heappush(num)
    else:
        if num < maxheap[-1]:
            minheap.heappush(maxheap.pop())
            maxheap.heappush(num):
        else:
            maxheap.heappush(num)

def track(numbers):
    #solution: use a maxheap and a minheap.
    for i in numbers:
        addNum(i)
    if len(maxheap) == len(minheap):
        return (maxheap.peek() + minheap.peek()) / 2
    else:
        return maxheap.peek()
