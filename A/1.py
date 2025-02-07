https://drive.google.com/file/d/1ZRmjTKL4WfZxjQyYC1YZ3shTj7DhmWsd/view?clckid=ff0de9a1
n = int(input())
x=0
for i in range(n):
    a = input()
    if '+' in a:
        x+=1
    if '-' in a:
        x-=1
print(x)
