'''
Three sum problem
'''

# Brute-force algorithm
class ThreeSum1:
    def __init__(self, nums) -> None:
        self.nums = nums

    def count(self):
        len_list = len(self.nums)
        count = 0
        for i in range(len_list):
            for j in range(1, len_list):
                for k in range(2, len_list):
                    if self.nums[i] + self.nums[j] + self.nums[k] == 0:
                        count += 1
        return count


# using binary search
class ThreeSum2:
    def __init__(self, nums) -> None:
        self.nums = nums

    def count(self):
        self.nums.sort()
        len_list = len(self.nums)
        count = 0
        for i in range(len_list):
            for j in range(1, len_list):
                if -(self.nums[i] + self.nums[j]) in self.nums:
                    count += 1
        return count