#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

priority_stack = []
key = []
left = []
right = []

def stackLeftNodes(index):
    if left:
        while left[index] != -1:
            priority_stack.append(index)
            index = left[index]
        priority_stack.append(index)


def IsBinarySearchTree():
    stackLeftNodes(0)
    check_if_binary = []
    visited_stack = [None]
    while priority_stack:
        top_of_stack = priority_stack.pop()
        check_if_binary.append(top_of_stack)
        if len(check_if_binary) > 1:
            if check_if_binary[-2] == visited_stack[-1]:
                if key[check_if_binary[-1]] < key[check_if_binary[-2]]:
                    return False
                visited_stack.pop()
            elif key[check_if_binary[-1]] <= key[check_if_binary[-2]]:
                return False
        if right[top_of_stack] != -1:
            visited_stack.append(top_of_stack)
            stackLeftNodes(right[top_of_stack])
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    for node in tree:
        key.append(node[0])
        left.append(node[1])
        right.append(node[2])
    if IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
