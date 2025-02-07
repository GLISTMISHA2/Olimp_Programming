https://codeforces.com/contest/2044/problem/B
t = int(input())
for di in range(t):
    a = list(input())
    pb = a[::-1]
    b =[]
    for i in pb:
        if i == 'q':
            b.append('p')
        if i == 'p':
            b.append('q')
        if i == 'w':
            b.append('w')
    print("".join(b))
