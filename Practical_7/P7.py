#Given two numbers x,y
# . You need to determine if there exists an integer n
#  such that S(n)=x
# , S(n+1)=y
# .
#
# Here, S(a)
#  denotes the sum of the digits of the number a
#  in the decimal numeral system.
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers x,y
#  (1≤x≤1000,1≤y≤1000
# ).
#
# Output
# For each test case, print "NO" if a suitable n
#  does not exist. Otherwise, output "YES".
#
# Example
# Input
# 7
# 1 2
# 77 77
# 997 999
# 999 1
# 1000 1
# 1 11
# 18 1
# Output
# Yes
# No
# No
# Yes
# No
# No
# Yes

def digit_sum(num):
    return sum(int(d) for d in str(num))

def solve():
    t = int(input())
    results = []

    for _ in range(t):
        x = int(input(""))
        y = int(input(""))

        found = False
        for n in range(1, 10000):  # Restrict n to reasonable range
            if digit_sum(n) == x and digit_sum(n + 1) == y:
                found = True
                break

        if found:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))

solve()