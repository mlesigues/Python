#Task: Maximum XOR of Two Numbers in an Array
#src: https://www.youtube.com/watch?v=wSgrc98d2lI&list=LLAFn5PITDRNXdxyWh0QMQxg&index=2
class TrieNode:
    #constructor
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insertBits(self, num):
        #convert num into binary then add it into trie
        bit_number = bin(num)[2:].zfill(32)
        #we get 0bxxxxx, therefore skip the first 2 elems; then fill it up until we have 32 elements
        
        node = self.root #always start at root
        for bit in bit_number:
            if bit not in node.children: #if the bit does not exist
                node.children[bit] = TrieNode()
            
            node = node.children[bit]
            
    def findMax_xor(self, num):
        bit_number = bin(num)[2:].zfill(32)
        node = self.root
        max_xor = ' ' #will hold the max xor values
        
        for bit in bit_number:
            if bit == '0':
                opposite_bit = '1'
            elif bit == '1':
                opposite_bit = '0'
                
            if opposite_bit in node.children: #check if opposite bit exists in children nodes
                max_xor += opposite_bit
                node = node.children[opposite_bit]
                
            else: #it does not exist
                max_xor += bit
                node = node.children[bit]
                
        return int(max_xor, 2) ^ num #perform xor operation here
        
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        #use of trie!
        for elems in nums:
            self.insertBits(elems)
            
        max_ = 0
        for elems in nums:
            max_ = max(max_, self.findMax_xor(elems))
        
        return max_

    
    
    
#Task: Day 7: Pearson Correlation Coefficient I from Hackerrank Statistics
import math

n = int(input())
data_set_X = list(map(float, input().strip().split())) #ensures we get 1 elem at a time
data_set_Y = list(map(float, input().strip().split()))

#calculate(mu * x) and (mu * y) these are both means of X and Y, respectively
#to get mean, sum all the trials and divide by how many trial times
mu_x = sum(data_set_X)/n
mu_y = sum(data_set_Y)/n

#calculate (sigma * X) and (sigma * Y) these are both standard deviations of X and Y
stdDev_x = math.sqrt(sum([(elem - mu_x)**2 for elem in data_set_X]) / n)
stdDev_y = math.sqrt(sum([(elem - mu_y)**2 for elem in data_set_Y]) / n)

#compute covariance; cov(X,Y)
cov_x_y = sum([(data_set_X[i] - mu_x) * (data_set_Y[i] - mu_y) for i in range (n)])

#compute Pearson Correlation Coefficient
pearson_correlation_coeff = cov_x_y/(stdDev_x * stdDev_y*n)

print(round(pearson_correlation_coeff, 3))




#Task: Day 7:
