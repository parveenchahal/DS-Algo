class Solution:
    # @param A : list of strings
    # @return an integer

    def get_bucket(self, A):
        buckets = [None] * 20
        for x in A:
            if x[0] >= '2':
                continue
            base = 0
            if x[0] == '1':
                base = 10
            ind = base + int(x[2])
            try:
                if len(buckets[ind]) < 3:
                    buckets[ind].append(x)
            except:
                buckets[ind] = [x]
        return buckets
        

    def solve(self, A):
        buckets = self.get_bucket(A)
        li = []
        for bucket in buckets:
            if bucket is not None:
                for x in bucket:
                    li.append(float(x))
        l = len(li)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    s = li[i] + li[j] + li[k]
                    if s > 1 and s < 2:
                        return 1
        return 0


s = Solution()
A =  [ "0.234022", "0.051717", "0.820402", "0.492629", "0.004825", "0.589073" ]
r = s.solve(A)
assert r == 1

A = [ "0.651154", "0.105475", "2.154505", "1.901806", "0.950285", "0.934355", "0.165230", "1.337531" ]
r = s.solve(A)
assert r == 1

A = [ "2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191" ]
r = s.solve(A)
assert r == 1

A = [ "0.503094", "0.648924", "0.999298" ]
r = s.solve(A)
assert r == 0