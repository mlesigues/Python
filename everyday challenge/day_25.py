#Task: Iterator for Combination
#src: https://www.youtube.com/watch?v=PmLiLPsb__4
class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        #takes a string of chars of sorted distinct lowercase English letters and a number of 
        #combinationLength
        #easy: use library called itertools
        self.result = itertools.combinations(characters, combinationLength) 
        #(line above) this will return a list of tuples that contains all the possible combinations

        #regenate the tuples to become string, using join()
        self.result = ["".join(tups) for tups in self.result]

        #need counter; this is needed for the next() & hasNext()
        self.counter = -1 #points to -1 because we have not started yet
        

    def next(self) -> str:
        #returns the next combination of length combinationLength in 
        #lexicographical order/dictionary order

        #if there is a next combination, increase the counter by 1
        #then return the current index string 
        if self.hasNext():
            self.counter +=1
            return self.result[self.counter]
        
        
    
    def hasNext(self) -> bool:
        return self.counter + 1 < len(self.result)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()