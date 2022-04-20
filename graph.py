from collections import defaultdict 
graph = defaultdict(list)
graph[1].append(2) # 1-> 2
graph[2].append(3) # 1-> 2 -> 3
graph[3].append(4) # 1-> 2 -> 4

visited = set()
def dfs(node,graph,visited):
   if node not in visited:
      print(node)
      visited.add(node)
      for v in graph[node]:
         dfs(v,graph, visited)
dfs(4, graph , visited)         