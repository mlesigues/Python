#Add and Search Word Data from Leetcode!
class WordDictionary:
    
#src: https://medium.com/@lenchen/leetcode-211-add-and-search-word-data-structure-design-3498402a8099
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        """
        temp_trie = self.trie
        for letters in word:
            if letters not in temp_trie:
                temp_trie[word] = {}
            temp_trie = temp_trie[word]
        temp_trie['#'] = '#'
        """
        curr = self.trie
        for letter in word:
            curr = curr.setdefault(letter,{})
        curr['_end_'] = word
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        """
        temp_trie = self.trie
        for letters in word:
            if letters not in temp_trie:
                return False
            temp_trie = temp_trie[word]
        if '#' in temp_trie:
            return True
        return False
        """
        return self.repeatSearch(word, len(word), self.trie)
    
    def repeatSearch(self, word, length, node):
        if type(node) is not dict:
            return False
        
        curr = node
        for i in range(len(word)):
            letter = word[i]
            
            if letter == '.':
                return any([self.repeatSearch(word[i+1:], length, curr[child]) for child in curr])
            
            if letter not in curr:
                return False
            
            curr = curr[letter]
            
        return len(curr.get('_end_', '')) == length


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

#Task: Implement Trie (Prefix Trie)
class Trie:
    #you may assume that all inputs are consist of lowercase letters, a-z
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        """
        temp_trie = self.trie
        for letters in word:
            if letters not in temp_trie:
                temp_trie[word] = {}
            temp_trie = temp_trie[word]
        temp_trie['#'] = '#'
        """
        
        temp_trie = self.trie
        for letters in word:
            temp_trie = temp_trie.setdefault(letters, {})
        temp_trie['_end_'] = word
        
       
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        return self.startsWith(word + '#')
          

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp_trie = self.trie
        for word in prefix:
            if word not in temp_trie:
                return False
            temp_trie = temp_trie[word]
        return True           
        
    
          

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)