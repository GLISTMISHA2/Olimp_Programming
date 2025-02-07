https://codeforces.com/contest/2044/problem/A
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0

    for a in range(1, n):
        for b in range(1, n):
            if a + b == n:
                count += 1 

    print(count) 
