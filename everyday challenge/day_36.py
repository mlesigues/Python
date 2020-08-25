#Task: Squares of a Sorted Array from Leetcode

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #sort it ascending order, and square the elements
        
        """
        elemSquare = []
        
        for elems in range(0, len(A)):
            square = elems ** 2
            elemSquare.append(square)
        return elemSquare
        """

        #src: https://www.kite.com/python/answers/how-to-square-the-elements-of-a-list-in-python#:~:text=Use%20a%20list%20comprehension%20to,of%20each%20number%20in%20list%20.
        squares = [elems ** 2 for elems in A]
        squares.sort()
        
        return squares

        
        