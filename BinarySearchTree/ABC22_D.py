import bisect
def is_ok(upper_height):
    time = []
    for i in range(N):
        time.append((upper_height-B[i])//A[i])
    time.sort()
    for n in range(N):
        if (time[n] < n):
            return False  # 時間ぎれ
    return True


def binary_search(left, right):
    while(abs(right-left) > 1):
        mid = (right+left)//2
        if(is_ok(mid)):
            right = mid
        else:
            left = mid
    return right

N = int(input())
B = []
A = []
for n in range(N):
    b, a = map(int, input().split())
    B.append(b)
    A.append(a)

left = 0
right = 1e+14

print(int(binary_search(left, right)))
