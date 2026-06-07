class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s)-1
        while (left < right) and left < len(s) and right > -1:
            if ((s[left]>'z' or s[left]<'a') and (s[left]>'9' or s[left]<'0')):
                left += 1
                if left == len(s)-1:
                    break
            elif ((s[right]>'z' or s[right]<'a') and (s[right]>'9' or s[right]<'0')):
                right -= 1
                if right == 0:
                    break
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True