#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def inOrder(tree,root,result=None):
    if result is None:  # create a new result if no intermediate was given (for recursion)
        result = []
    
    if root == -1:
            return
    inOrder(tree,tree[root][1],result) #left child
    result.append(tree[root][0])
    inOrder(tree,tree[root][2],result) #right child
    return result

def isBST(tree):

    result = inOrder(tree,0)

    x = result[0]

    for i in range(len(result)):
        if result[i] < x:
            return False
        x = result[i]
    return True
        


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if len(tree) <= 1 or isBST(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
