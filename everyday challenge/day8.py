#TASK: LIST COMPREHENSIONS! YOU ARE GIVEN THREE INTEGERS x, y, and z
#REPRESENTING THE DIMENSIONS OF A CUBOID ALONG WITH AN INTEGER n. PRINT
#A LIST OF ALL POSSIBLE COORDINATED GIVEN BY (i,j,k) ON A GRID 3D WHERE
#THE SUM OF i+j+k IS NOT EQUAL TO n. HERE, 0<=i<=x; 0<=j<=y, o<=k<=z. USE
#LIST COMPREHENSIONS RATHER THAN MULTIPLE LOOPS.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #need to list all permutations of x,y,z using list
    # for i in range(x+1):
    #     print(x)
    #     for j in range(y+1):
    #        print(y)
    #         for k in range(z+1):
    #             if(i+j+k != n):
                    
    #                 print([i,j,k],end="")

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

  #TASK: YOU ARE GIVEN A STRING. SPLIT THE STRING ON A " "(space) DELIMETER AND JOIN USING A "-" hypen.
def split_and_join(line):
        # write your code here
    newSplit = line.split(" ") #split by space delimeter
    newJoin = "-".join(newSplit) #join by hypen

    return newJoin


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#TASK: Given an array, A, of N, integers, print each element in reverse order as a single line of
#space-separated integers.

#input format: first line contains integer N (the # of integers in A)
#              second line contains N space-separated integers describing A
#Constraints: 1<=N<=10^3, 1<=A_i<=10^4 where A_i is the ith integers in A
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    temp = []
    for i in range(len(a)):
        temp.append(a[len(a)-i-1])
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

#TASK: LINKED LISTS. 
#INPUT: The first line of input contains, n, the number of elements in the linked list.
#The next n lines contain one element each, which are the elements of the linked list.
#CONSTRAINTS: 1<=n<=1000, 1<=list_i<=1000, where list_i is the ith element of the linked list.

#!/bin/python3
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def printLinkedList(head):
    #Complete logic here
    if head is not None:
        print(head.data)
        printLinkedList(head.next)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)


#TASK: You're given the pointer to the head of a linked list and an integer to add to
#the list. Create a new node with the given integer, insert this node at the head of the 
#linked list and return the new head node. The head pointer given may be null meaning that
#the initial list is empty.
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    newNode.next = llist

    return newNode
    #return SinglyLinkedListNode(data)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()

