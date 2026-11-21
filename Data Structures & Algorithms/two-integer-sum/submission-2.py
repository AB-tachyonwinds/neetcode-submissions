class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if d.get(difference, None) != None:
                return [d.get(difference), i]
            else:
                d[nums[i]] = i
            
        return [-1, -1]
