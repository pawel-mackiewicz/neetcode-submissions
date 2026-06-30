class Tree:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start, end):
        s = self.start
        e = self.end

        if start >= e:
            if not self.right:
                self.right = Tree(start,end)
                return True
            return self.right.insert(start,end)
        elif end <= s:
            if not self.left:
                self.left = Tree(start,end)
                return True
            return self.left.insert(start,end)
        else:
            return False
            


class MyCalendar:
    
    def __init__(self):
        self.tree = None


    def book(self, startTime: int, endTime: int) -> bool:
        if not self.tree:
            self.tree = Tree(startTime, endTime)
            return True
        
        return self.tree.insert(startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)