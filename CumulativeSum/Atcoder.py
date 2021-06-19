N = int(input())
A = list(map(int, input().split()))
CS = [0]
for i, v in enumerate(A):
    CS.append(v+CS[i])
for i in range(1,len(A)+1,1):
    ans = []
    for j in range(len(A), -1, -1):
        ans.append(CS[j]-CS[j-i])
    print(max(ans))
