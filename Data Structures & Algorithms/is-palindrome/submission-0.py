class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)
        first_half = []
        second_half = []

        for i in range(n//2):

            first_half.append(s[i])

        for i in range(-1, -(n//2)-1,-1):
            second_half.append(s[i])

        if first_half == second_half:
            return True
        else:
            return False