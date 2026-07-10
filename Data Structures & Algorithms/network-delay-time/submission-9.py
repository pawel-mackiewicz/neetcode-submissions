class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsedT = 0
        visited = set()

        nodes = collections.defaultdict(list)
        for source, target, time in times:
            nodes[source].append((time, target))
        
        minHeap = [(0,k)]

        while minHeap:
            time, target = heapq.heappop(minHeap)

            if target in visited:
                continue
            visited.add(target)
            
            if len(visited) == n:
                return time

            for time2, target2 in nodes[target]:
                if target2 not in visited:
                    heapq.heappush(minHeap, (time2 + time, target2))
        
        return -1