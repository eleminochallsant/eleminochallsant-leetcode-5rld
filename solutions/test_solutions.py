"""Run all LeetCode solution tests."""
import sys
sys.path.insert(0, ".")
from solutions_0001_two_sum import Solution as TwoSum
from solutions_0009_palindrome import Solution as Palindrome


def test_two_sum():
    s = TwoSum()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_palindrome():
    s = Palindrome()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False


if __name__ == "__main__":
    test_two_sum()
    test_palindrome()
    print("All tests passed!")
