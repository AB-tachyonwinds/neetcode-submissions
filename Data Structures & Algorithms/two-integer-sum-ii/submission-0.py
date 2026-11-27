class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x, y = 0, len(numbers)-1

        while x < y:
            result = numbers[x] + numbers[y]
            if result == target:
                return [x+1, y+1]
            elif result < target:
                x += 1
            else:
                y -= 1
        