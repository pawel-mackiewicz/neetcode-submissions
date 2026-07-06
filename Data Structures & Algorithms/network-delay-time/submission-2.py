class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        delay = 0

        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0,k)]

        while minHeap and len(visited) != n:
            t1, v1 = heapq.heappop(minHeap)

            if v1 in visited:
                continue
            visited.add(v1)

            delay = t1

            for v2, t2 in edges[v1]:
                heapq.heappush(minHeap, (t2+t1,v2))

        return delay if len(visited) == n else -1