class TreeNode:

    def __init__(self):
        self.chars = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.node = TreeNode()


    def insert(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TreeNode()
            curr = curr.chars[c]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.node
        for c in word:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for c in prefix:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        return True
        