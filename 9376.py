from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,x,y):
    r = len(a)
    c = len(a[0])
    dist = [[-1]*c for _ in range(r)]
    d = deque()
    d.append((x,y))
    dist[x][y] = 0
    while d:
        x,y = d.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] +1
                    d.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    d.appendleft((nx,ny))
    return dist


n = int(input())
for _ in range(n):
    h,w = map(int,input().split())
    a=['.'+input()+'.' for _ in range(h)]
    h+=2
    w+=2
    a = ['.'*w] + a + ['.'*w]
    x1=x2=y1=y2=-1
    for i in range(h):
        for j in range(w):
            if a[i][j] == '$':
                if x1 == -1:
                    x1,y1 = i,j
                else:
                    x2,y2 = i,j
    d0 = bfs(a,0,0)
    d1 = bfs(a,x1,y1)
    d2 = bfs(a,x2,y2)
    ans = 100000
    for i in range(h):
        for j in range(w):
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] ==-1 or d2[i][j] ==-1:
                continue
            hap = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                hap -= 2
            ans = min(ans,hap)
    print(ans)




