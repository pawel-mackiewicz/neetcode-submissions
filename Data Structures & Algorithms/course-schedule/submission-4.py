class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = {}

        for a,b in prerequisites:
            if not pre.get(a):
                pre[a] = []
            if not pre.get(b):
                pre[b] = []
            pre[a].append(b)

        finished = set()
        visited = set()

        def dfs(n):
            if n not in pre:
                finished.add(n)
                # visited.add(n)
            if n in finished:
                return True
            if n in visited:
                return False

            visited.add(n)

            for course in pre[n]:
                if not dfs(course):
                    return False
            finished.add(n)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            