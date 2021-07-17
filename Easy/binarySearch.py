class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            center = (upper + lower)//2
            if target == nums[center]:
                return center
            elif target > nums[center]:
                lower = center+1
            else:
                upper = center-1
        return -1
