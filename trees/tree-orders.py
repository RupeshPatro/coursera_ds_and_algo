# python3

import sys, threading
sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.prioritystack = []

    # def read(self):
    #     # self.n = int(sys.stdin.readline())
    #     temp = 6
    #     self.n = temp
    #     self.key = [0 for i in range(self.n)]
    #     self.left = [0 for i in range(self.n)]
    #     self.right = [0 for i in range(self.n)]
    #     # for i in range(self.n):
    #     # [a, b, c] = map(int, sys.stdin.readline().split())
    #     # self.key[i] = a
    #     # self.left[i] = b
    #     # self.right[i] = c
    #     # readlines_ = ['4 1 2', '2 3 4', '5 -1 -1', '1 -1 -1', '3 -1 -1']
    #     # readlines_ = ['0 7 2', '10 -1 -1', '20 -1 6', '30 8 9', '40 3 -1', '50 -1 -1', '60 1 -1', '70 5 4', '80 -1 -1', '90 -1 -1']
    #     # readlines_ = ['1 1 2', '2 -1 -1', '3 -1 -1']
    #     # readlines_ = ['1 -1 -1']
    #     # readlines_ = ['1 1 -1', '2 -1 -1']
    #     # readlines_ = ['0 -1 1', '20 -1 2', '60 3 -1', '10 -1 -1']
    #     # readlines_ = ['0 1 -1', '1 -1 2', '2 3 -1', '3 -1 4', '4 5 -1', '5 -1 -1']
    #     readlines_ = ['0 -1 1', '1 2 -1', '2 -1 3', '3 4 -1', '4 -1 5', '5 -1 -1']
    #     for i in range(temp):
    #         [a, b, c] = map(int, readlines_[i].split())
    #         self.key[i] = a
    #         self.left[i] = b
    #         self.right[i] = c
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def stackLeftNodes(self, index):
        while self.left[index] != -1:
            self.prioritystack.append(index)
            index = self.left[index]
        self.prioritystack.append(index)

    def stackAndAppend(self, index):
        while self.left[index] != -1:
            self.prioritystack.append(index)
            self.result.append(self.key[index])
            index = self.left[index]
        self.prioritystack.append(index)
        self.result.append(self.key[index])

    def inOrder(self):
        self.result = []
        self.stackLeftNodes(0)
        while self.prioritystack:
            top_of_stack = self.prioritystack.pop()
            self.result.append(self.key[top_of_stack])
            if self.right[top_of_stack] != -1:
                self.stackLeftNodes(self.right[top_of_stack])
        return self.result

    def preOrder(self):
        self.result = []
        self.stackAndAppend(0)
        while self.prioritystack:
            top_of_stack = self.prioritystack.pop()
            if self.right[top_of_stack] != -1:
                self.stackAndAppend(self.right[top_of_stack])
        return self.result

    def postOrder(self):
        self.result = []
        self.visited_stack = []
        self.stackLeftNodes(0)
        while self.prioritystack:
            top_of_stack = self.prioritystack[-1]
            if self.visited_stack:
                if top_of_stack == self.visited_stack[-1]:
                    self.visited_stack.pop()
                    self.result.append(self.key[self.prioritystack.pop()])
                    continue
            if self.right[top_of_stack] != -1:
                while self.right[top_of_stack] != -1:
                    self.visited_stack.append(top_of_stack)
                    self.stackLeftNodes(self.right[top_of_stack])
                    top_of_stack = self.prioritystack[-1]
            self.result.append(self.key[self.prioritystack.pop()])
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()