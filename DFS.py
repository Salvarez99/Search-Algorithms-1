import numpy as np


class DFS:

    stack = []

    # a dictionary representing node ASCII values and pairing to index position on an array
    vertices = {0: 'A',
                1: 'B',
                2: 'C',
                3: 'D',
                4: 'E',
                5: 'F',
                6: 'G',
                7: 'H',
                8: 'P',
                9: 'Q',
                10: 'R',
                11: 'S'}

    # Implementation of an iterative DFS on a vertex list
    # param_1: start: str
    # param_2: vertex_list: dict[str, list[str]]
    # param_3: visited: dict[str: bool]
    # return:
    @classmethod
    def DFS_stack_iterative_v(self, start: str, vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        self.stack = [start]

        while not self.isEmpty(self):
            node = self.stack.pop()
            neighbors = vertex_list.get(node)
            print(f"->{node}", end="")

            if node == 'G':
                return

            if neighbors:
                for neighbor in reversed(neighbors):
                    if visited.get(neighbor) == False:
                        visited[neighbor] = True
                        self.stack.append(neighbor)

        return

    # Implementation of an iterative DFS on an adjacency matrix
    # param_1: start: int
    # param_2: adj_matrix: np.ndarray
    # param_3: visited: dict[str: bool]
    # return:
    @classmethod
    def DFS_stack_iterative_adj(self, start: int, adj_matrix: np.ndarray, visited: dict[str: bool]):

        self.stack = [start]

        while not self.isEmpty(self):
            node = self.stack.pop()
            print(f"->{self.vertices.get(node)}", end="")

            if node == 6:
                return

            for col in reversed(range(len(adj_matrix))):
                node_key = self.vertices.get(col)

                if adj_matrix[node][col] == 1 and visited.get(node_key) == False:
                    visit = self.vertices.get(col)
                    visited[visit] = True

                    self.stack.append(col)

        return

    # Implementation of a recursive DFS on a vertex list
    # param_1: startNode: str
    # param_2: goalNode: str
    # param_3: vertex_list: dict[str, list[str]]
    # param_4: visited: dict[str: bool]
    # return: boolean
    @classmethod
    def DFS_stack_recursive_v(self, startNode: str, goalNode: str, vertex_list: dict[str, list[str]], visited: dict[str: bool]):

        visited[startNode] = True
        self.stack.append(startNode)
        print(f"->{startNode}", end="")

        if startNode == goalNode:
            return True

        neighbors = vertex_list.get(startNode)

        if neighbors:
            for neighbor in neighbors:
                if visited.get(neighbor) == False and neighbor not in self.stack:
                    visited[neighbor] = True
                    if self.DFS_stack_recursive_v(neighbor, goalNode, vertex_list, visited):
                        return True

        return False

    # Implementation of a recursive DFS on an adjacency matrix
    # param_1: startNode: int
    # param_2: goalNode: int
    # param_3: adj_matrix: np.ndarray
    # param_4: visited: dict[str: bool]
    # return: boolean
    @classmethod
    def DFS_stack_recursive_adj(self, startNode: int, goalNode: int, adj_matrix: np.ndarray, visited: dict[str: bool]):
        nodeLetter = self.vertices.get(startNode)
        visited[nodeLetter] = True
        self.stack.append(startNode)
        print(f"->{nodeLetter}", end="")

        if startNode == goalNode:
            return True

        for col in range(len(adj_matrix)):
            neighborLetter = self.vertices.get(col)

            if (adj_matrix[startNode][col] == 1) and (visited.get(neighborLetter) == False) and (col not in self.stack):
                if self.DFS_stack_recursive_adj(col, goalNode, adj_matrix, visited):
                    return True

        return False

    # Helper method to check if stack is empty
    # return: boolean
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    # Helper Method to empty stack
    # return:
    @classmethod
    def emptyStack(self):
        self.stack.clear()
