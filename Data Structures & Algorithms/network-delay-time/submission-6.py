class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsedT = 0
        visited = set()

        tt = collections.defaultdict(list)
        for source, target, time in times:
            tt[source].append((time, target))
        
        minHeap = [(0,k)]

        while minHeap and len(visited) < n:
            time, target = heapq.heappop(minHeap)

            if target in visited:
                continue
            visited.add(target)
            
            elapsedT = time

            for time2, target2 in tt[target]:
                heapq.heappush(minHeap, (time2 + elapsedT, target2))
        
        return elapsedT if len(visited) == n else -1