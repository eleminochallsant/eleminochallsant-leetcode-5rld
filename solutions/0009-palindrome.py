"""9. Palindrome Number
Difficulty: Easy
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    print("All tests passed!")
