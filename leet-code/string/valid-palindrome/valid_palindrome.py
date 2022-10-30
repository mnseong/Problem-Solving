from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        deq = deque()
        for char in s:
            if char.isalnum():
                deq.append(char.lower())
        while len(deq) > 1:
            if deq.popleft() != deq.pop():  # pop(0)-> O(n) vs popleft(), pop() -> O(1)
                return False
        return True


solve = Solution()

testcase1 = "A man, a plan, a canal: Panama"
testcase2 = "race a car"
testcase3 = ""
testcase_list = list(map(lambda x: solve.isPalindrome(x), [testcase1, testcase2, testcase3]))

print(*testcase_list)
