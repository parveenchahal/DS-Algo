# https://leetcode.com/problems/shuffle-an-array/


class Solution:

    def __init__(self, nums: List[int]):
        self._original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        suffle_array = list(self._original)
        n = len(suffle_array)
        last_index = n - 1
        for i in range(last_index):
            rand_idx = random.randint(i, last_index)
            suffle_array[i], suffle_array[rand_idx] = suffle_array[rand_idx], suffle_array[i]
        return suffle_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
