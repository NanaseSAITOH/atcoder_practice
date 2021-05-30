a, b, c = input().split()

if(a == b):
    print(c)
elif(a == c):
    print(b)
elif(b == c):
    print(a)
elif(a==b==c):
    print(a)
else:
    print(0)

