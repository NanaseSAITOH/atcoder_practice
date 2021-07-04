Yen = []
Yen.append(3628800)
Yen.append(362880)
Yen.append(40320)
Yen.append(5040)
Yen.append(720)
Yen.append(120)
Yen.append(24)
Yen.append(6)
Yen.append(2)
Yen.append(1)
P = int(input())
ans = 0
nokori = P
for i in Yen:
    if(nokori%i != nokori):
        ans += nokori // i
    nokori = nokori%i
print(ans)
