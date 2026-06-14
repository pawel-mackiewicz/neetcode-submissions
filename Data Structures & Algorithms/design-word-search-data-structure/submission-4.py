class DictNode:

    def __init__(self):
        self.childs = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.node = DictNode()
        

    def addWord(self, word: str) -> None:
        curr = self.node

        for c in word:
            if c not in curr.childs:
                curr.childs[c] = DictNode()
            curr = curr.childs[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def lookup_word(node: DictNode, index: int) -> bool:
                if index >= len(word):
                    return node.word
        
                c = word[index]
                childs = node.childs
        
                if c == ".":
                    for child in childs.values():
                        if lookup_word(child, index+1):
                            return True
                    return False
                elif c not in childs:
                    return False
                return lookup_word(childs[c], index+1)
        return lookup_word(self.node, 0)
