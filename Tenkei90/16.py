N = int(input())
A, B, C = map(int, input().split())
fst = N % C
if(fst > B and (fst % B) > A):
    
