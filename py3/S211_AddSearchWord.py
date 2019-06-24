# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)

# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

class Node:
    def __init__(self, isWord=False):
        self.isWord = isWord
        self.path2Node = {}
        self.chars = []

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        itr = self.root
        for c in word:
            if c not in itr.path2Node:
                itr.path2Node[c]=Node()
                itr.chars+=[c]
            itr = itr.path2Node[c]
        if len(word) > 0:
            itr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        result = False
        stack=[[self.root, -1]]     #[current node, current char index]
        i = 0
        while stack and len(word) > 0:
            #try to find next valid PATH
            topNode, cldIdx = stack[-1]
            if cldIdx+1 >= len(topNode.chars) : #visited, 
                stack.pop()
                i-=1
            elif ((word[i] != '.' and word[i] in topNode.path2Node) or (word[i] == '.')) and cldIdx+1 < len(topNode.chars):
                # find next node to try
                nextTryNode = topNode.path2Node[word[i]] if word[i] != '.' else topNode.path2Node[topNode.chars[cldIdx+1]]
                # if found
                if i == len(word)-1 and nextTryNode.isWord:
                    return True
                #update visiting states, if '.' , try sibline, if not '.', then done
                stack[-1][1] = len(topNode.chars) if word[i] != '.' else stack[-1][1] + 1
                #push to stack
                if i < len(word)-1:
                    stack+=[[nextTryNode, -1]]
                    i+=1
            #set to visited
            else:
                stack[-1][1] = len(topNode.chars)

        return result            

    def search(self, word: str) -> bool:






# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
# obj.addWord("akcdf")
# obj.addWord("bed")
print(obj.search(""))
