class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def key(interval):
    return (interval.start, interval.end)

def merge(intervals):
    n = len(intervals)
    if n < 2:
        return intervals
    intervals = sorted(intervals, key=key)
    i = 0
    result = []
    while i < n:
        cur_int = Interval(intervals[i].start, intervals[i].end)
        i += 1
        while i < n:
            if intervals[i].start <= cur_int.end:
                cur_int = Interval(min(cur_int.start, intervals[i].start), max(cur_int.end, intervals[i].end))
                i += 1
            else:
                break
        result.append(cur_int)
    return result


r = merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)])
print(r)