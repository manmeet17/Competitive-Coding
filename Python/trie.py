class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr=self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]]=TrieNode()
            curr=curr.children[word[i]]
        curr.end=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr=self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr=curr.children[word[i]]
        return curr.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr=self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr=curr.children[prefix[i]]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
param_2 = obj.search("word")
param_3 = obj.startsWith("wor")