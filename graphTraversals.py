import Queue

graph = { 
'A' : ['B','D', 'G'],
'B' : ['A' , 'E' , 'F'],
'C' : ['F','H'],
'D' : ['A','F'],
'E' : ['B','G'],
'F' : ['B','C','D'],
'G' : ['A','E'],
'H' : ['C']
}

def dfs(graph,start):
    ret=[]
    stack=start and [start]
    while stack:
        node=stack.pop()
        if node not in ret:
            ret.append(node)
            stack.extend(x for x in graph[node] if x not in ret)

    return ret

def bfs(graph,start):
    ret=[start]
    queue=[start]
    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if n not in ret:
                ret.append(n)
                queue.append(n)

    return ret


print bfs(graph,'A')
print dfs(graph,'A')
