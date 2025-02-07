https://drive.google.com/file/d/1ZRmjTKL4WfZxjQyYC1YZ3shTj7DhmWsd/view?clckid=ff0de9a1
n,k = map(int,input().split())
s = list(map(int,input().split()))
count = 0
m = k-1
for i in range(m+1,n):
    if s[m]>s[i]:
        print(i)
        break
