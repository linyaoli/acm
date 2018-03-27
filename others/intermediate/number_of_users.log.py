"""
given:
<'a', 5, 10>
<'b', 6, 8>
<'c', 10, 11>

assume input is a list of tuples, and ordered by the start time of a log.

"""
import collections

def logger(users):
    record = {}
    for i in users:
        try:
            record[i[1]] += 1
        except:
            record[i[1]] = 1

        try:
            record[i[2]] -= 1
        except:
            record[i[2]] = -1
    num = 0
    ret = []
    record = collections.OrderedDict(sorted(record.items()))
    for i in record:
        num += record[i]
        ret.append((i, num))
    return ret


print logger([('a', 5, 10), ('b', 6, 8), ('c', 10, 11)])
