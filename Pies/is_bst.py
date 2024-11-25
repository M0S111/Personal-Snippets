#!/usr/bin/python3

import sys, threading, math

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

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
    #result = result[:math.ceil(len(result))]

    for i in range(1,len(result[:math.ceil(len(result))])):
        if result[i-1] > result[i] or result.count(result[i-1]) > 1:
            return False
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
