#Fizz Buzz from Leetcode
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #divisibility rule of 3 and 5
        #multiple of 3: fizz
        #multiple of 5: buzz
        #multiple of 3 & 5: fizzbuzz
        
        #some strategies:
        #go through n, convert n to string 
        #append everything at the end!
        
        elemList = []
        
        for elem in range(1, n+1): #skip 0? so start at 1, end at n+1
            n = str(elem)
            if elem % 15 == 0: #divisible by both 3 & 5
                n = "FizzBuzz"
            elif elem % 5 == 0:
                n = "Buzz"
            elif elem % 3 == 0: 
                n = "Fizz"
                
            elemList.append(n)
            
        return elemList
                