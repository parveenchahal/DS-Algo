# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution:
    
    def find_just_greater_from_right(self, num, n, i, x):
        for t in range(n - 1, i - 1, -1):
            if num[t] > x:
                return t
        return -1
    
    def next_permutation(self, num, n):
        
        for i in range(n - 2, -1, -1):
            if num[i] < num[i + 1]:
                j = self.find_just_greater_from_right(num, n, i + 1, num[i])
                num[i], num[j] = num[j], num[i]
                for t in range(0, (n - i) // 2):
                    num[t + i + 1], num[n - 1 - t] = num[n - 1 - t], num[t + i + 1]
                return
        
    def getMinSwaps(self, num: str, k: int) -> int:
        n = len(num)
        org_num = list(num)
        num = list(num)
        kth_larger = num
        while k > 0:
            self.next_permutation(kth_larger, n)
            k -= 1
        count = 0
        for i in range(n):
            if num[i] == org_num[i]:
                continue
            for j in range(i + 1, n):
                if num[i] == org_num[j]:
                    for k in range(j, i, -1):
                        org_num[k] = org_num[k - 1]
                        count += 1
                    break
        return count

r = Solution().getMinSwaps("5489355142", 4)
print(r)