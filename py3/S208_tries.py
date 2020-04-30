'''
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        itr = self.root
        for c in word:
            if c not in itr:
                itr[c] = {}
            itr = itr[c]
        itr['END'] = True    #结束符可以用任何有意义的关键字表示
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        itr = self.root
        for c in word:
            if c in itr:
                itr = itr[c]
            else:
                return False
        return 'END' in itr     #结束符很重要，区分中间节点和叶节点. 
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        itr = self.root
        for c in prefix:
            if c in itr:
                itr = itr[c]
            else:
                return False
        return True
             
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)