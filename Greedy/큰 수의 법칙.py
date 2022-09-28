n,m,k = map(int,input().split())

num = list(map(int,input().split()))
num.sort(reverse=True)
x = m//k
y = m%k
answer = 0
answer+=num[0]*x*k
answer+=num[1]*y

print(answer)
