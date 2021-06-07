def is_ok(mid):
    a = mid
    b = mid
    for i in range(len(T)-1,-1,-2):
        if(a>=b):
            a -= T[i]
            if(i-1>=0):
                b -= T[i-1]
        else:
            b -= T[i]
            if(i-1 >= 0):
                a -= T[i-1]
    if(a>=0 and b>=0):
        return True
    else:
        return False


def binary_search(left, right):
    last = (right+left)//2
    while(abs(right-left) > 1):
        mid = (right+left)//2
        if(is_ok(mid)):
            right = mid
        else:
            left = mid
    if(is_ok(is_ok(left))):
        return(left)
    return right


N = int(input())
T = list(map(int, input().split()))
T.sort()
T = sorted(T)

left = 0
right = 10**3+1

print(int(binary_search(left, right)))
