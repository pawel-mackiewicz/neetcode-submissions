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
        return lookup_word(word, self.node)

def lookup_word(word: str, node: DictNode) -> bool:
        if word == "" or not word:
            return node.word

        c = word[0]
        childs = node.childs

        if c == ".":
            for child in childs.values():
                if lookup_word(word[1:], child):
                    return True
            return False
        elif c not in childs:
            return False
        return lookup_word(word[1:], childs[c])