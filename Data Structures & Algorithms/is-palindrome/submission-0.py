class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        one = 0
        two = len(s)-1

        while one < two:
            if s[one] != s[two]:
                return False
            one += 1
            two -= 1

        return True