class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop and place all of the values in a hashmap where the key is the index and the value is the  number
        d = {}

        # loop with n and subtract from target

        for i in range(len(nums)):
            difference = target - nums[i]
            if d.get(difference, None) != None:
                return [d.get(difference), i]
            else:
                d[nums[i]] = i
            
        return [-1, -1]



        # check in dictionary if the difference exists
        # keep looping if otherwise
        # return list with smallest indice first
        