class Solution:
    def reorderLogFiles(self, logs: list) -> list:
        letters, digits = [], []
        for log in logs:
            tmp = log.split()
            if tmp[1].isdigit():
                digits.append(tmp)
            else:
                letters.append(tmp)
        print(letters, digits)
        return [" ".join(i) for i in sorted(letters, key=lambda x: (x[1:], [x[0]])) + digits]

    
solve = Solution()

testcase1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
testcase2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
testcase3 = ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]

testcase_list = list(map(lambda x: solve.reorderLogFiles(x), [testcase1, testcase2, testcase3]))

print(*testcase_list)