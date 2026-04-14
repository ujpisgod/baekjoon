import sys
sys.setrecursionlimit(100000)

def solve():
    data=sys.stdin.read().split()
    if not data:return
    V,E=int(data[0]),int(data[1])
    d={i:[]for i in range(1,V+1)}
    
    idx=2
    for _ in range(E):
        d[int(data[idx])].append(int(data[idx+1]))
        idx+=2
        
    dfn=0
    st=[0]*(V+1)
    low=[0]*(V+1)
    in_stack=[False]*(V+1)
    stack=[]
    scc_list=[]

    def dfs(cur):
        nonlocal dfn
        dfn+=1
        st[cur]=low[cur]=dfn
        stack.append(cur)
        in_stack[cur]=True
        
        for nxt in d[cur]:
            if st[nxt]==0:
                dfs(nxt)
                low[cur]=min(low[cur],low[nxt])
            elif in_stack[nxt]:
                low[cur]=min(low[cur],st[nxt])
                
        if st[cur]==low[cur]:
            scc=[]
            while True:
                node=stack.pop()
                in_stack[node]=False
                scc.append(node)
                if node==cur:break
            scc.sort()
            scc_list.append(scc)

    for i in range(1,V+1):
        if st[i]==0:dfs(i)

    scc_list.sort(key=lambda x:x[0])
    print(len(scc_list))
    for scc in scc_list:print(*scc,-1)

if __name__=='__main__':solve()