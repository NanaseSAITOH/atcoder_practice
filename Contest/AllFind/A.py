import sys
N = int(input())

def combination(n,r):
    kosuu = 1
    for i in range(0,r,1):
        kosuu = kosuu*(n-i)/(i+1)
    return kosuu


def calculate_yakusu(N):
    if(N%2==0):
        return 0
    ans = 0
    kotae = 0
    for i in range(1, int(N/2+1), 1):
        if(N % i == 0):
            ans += 1
            N = N/i
    ans -= 1
    for a in range(1, ans+1, 1):
        kotae += int(combination(ans, a))
    if(kotae+1 == 8):
        return 1
    else:
        return 0
ans2 = 0
for i in range(N+1):
    ans2 += calculate_yakusu(i)
print(ans2)

