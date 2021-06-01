def binary_search_tree(t):
    left = -1
    right = float(n)
    mid = int((right-left)/2)-1
    while(right-left > 1):
        if(s[mid] == t):
            return 1
        elif(s[mid] < t):
            left = mid
            mid = mid+int((right-left)/2)
        elif(s[mid] > t):
            right = mid
            mid = mid-int((right-left)/2)
    return 0

n = int(input())
s = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
ans = 0
for t in T:
    ans += binary_search_tree(t)
print(ans)
