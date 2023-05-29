import heapq
import os 
import math

def prims(n, edges, start):
    adj = [[] for _ in range(n)] 

    for u, v, weight in edges:
        u -= 1  
        v -= 1  

        if 0 <= u < n and 0 <= v < n:  
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        else:
            raise ValueError("Invalid vertex indices")

    visited = [False] * n  
    min_heap = [(0, start - 1)]  
    total_weight = 0  

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight

        for neighbor, edge_weight in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return total_weight


if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())

    edges = []

    for _ in range(m):
        u, v, weight = map(int, input().rstrip().split())
        edges.append((u, v, weight))

    start = int(input().strip())

    result = prims(n, edges, start)

    print(result)