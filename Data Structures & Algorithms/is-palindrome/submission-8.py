class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s)-1
        while (left < right) and left < len(s) and right > -1:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True