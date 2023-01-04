"""
"후위 표기식"
"https://www.acmicpc.net/problem/1918"
"""

import sys
input = sys.stdin.readline

numbers = list(input())
result = []

# in-stack precedence
def isp(s):
    if s == '*' or s == '/':
        return 2
    elif s == '(':
        return 0
    else:
        return 1


# in-coming precedence
def icp(s):
    if s == '*' or s == '/':
        return 2
    elif s == '(':
        return 3
    else:
        return 1


# 후위표기식
def calculate(list):
    stack = []
    for i in list:
        if i.isalpha():
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        elif i == '*' or i == '/':
            if not stack:
                stack.append(i)
            else:
                while stack and isp(stack[-1]) >= icp(i):
                    result.append(stack.pop())
                stack.append(i)
        elif i == '+' or i == '-':
            if not stack:
                stack.append(i)
            else:
                while stack and isp(stack[-1]) >= icp(i):
                    result.append(stack.pop())
                stack.append(i)
    while stack:
        result.append(stack.pop())

calculate(numbers)
postfix = ''.join(result)
print(postfix)