def dfs(x):
    for i in range(1,b+1):
        if l[x][i]==1:continue
        y=i
        if t[y]:continue
        t[y]=True
        if q[y]==0 or dfs(q[y]):
            q[y]=x
            return True
    return False
a,b,c=map(int,input().split())
l=[[0 for g in range(301)] for i in range(301)]
for g in range(c):
    d,e=map(int,input().split())
    l[d][e]=1
q=[0]*301
t=[0]*301
cnt=0
for i in range(a):
    t=[0]*301
    if dfs(i+1):
        cnt+=1
print(cnt)