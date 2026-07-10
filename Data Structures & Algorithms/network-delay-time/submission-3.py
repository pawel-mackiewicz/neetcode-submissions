class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # transform into list of [source] = (time, target)
        # push source == k to minHeap
        # traverse minHeap and push to heap
        # keep track of visited
        # make sure that you are not visiting same 2 times
        # when pushing to minHeap, time as time passed from the beggining
        # keep track of passed time
        # if visited.size == n return time else -1


        tt = collections.defaultdict(list)
        for source, target, time in times:
            tt[source].append((time, target))
        
        minHeap = []


        elapsedT = 0
        visited = set()

        for time, target in tt[k]:
            heapq.heappush(minHeap, (time,target))
        visited.add(k)

        while minHeap and len(visited) < n:
            time, target = heapq.heappop(minHeap)

            if target in visited:
                continue
            visited.add(target)
            
            elapsedT = time

            for time2, target2 in tt[target]:
                heapq.heappush(minHeap, (time2 + elapsedT, target2))
        
        return elapsedT if len(visited) == n else -1