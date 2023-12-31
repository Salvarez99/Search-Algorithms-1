import numpy as np


class convert:
    # an array representing node ASCII values
    letters = np.array(['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'P', 'Q', 'R', 'S'])

    # a dictionary representing node ASCII values and pairing to index position on an array
    vertices = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'P': 8,
        'Q': 9,
        'R': 10,
        'S': 11}

    # Takes in a given vertex list then converts it into an unweighted adjacency matrix
    # param_1: matrix: np.ndarray
    # param_2: vertex_list: dict[str, list[str]]
    # return: matrix: np.ndarray
    @classmethod
    def convertListToMatrixUW(self, matrix: np.ndarray, vertex_list: dict[str, list[str]]):
        for key, values in vertex_list.items():
            if key in self.vertices:
                row = self.vertices.get(key)
                for value in values:
                    col = self.vertices.get(value)
                    matrix[row][col] = 1

        return matrix

    # Takes in a given vertex list and edge list then converts it into a weighted adjacency matrix
    # param_1: matrix: np.ndarray
    # param_2: vertex_list: dict[str, list[str]]
    # param_3: edge_list: dict[str, list[int]]
    # return: matrix: np.ndarray
    @classmethod
    def convertListToMatrixW(self, matrix: np.ndarray, vertex_list: dict[str, list[str]], edge_list: dict[str, list[int]]):

        edgeIndex = 0
        for node, neighbors in vertex_list.items():
            if node in self.vertices:
                row = self.vertices.get(node)
                for neighbor in neighbors:
                    col = self.vertices.get(neighbor)
                    neighborsEdgeCost = edge_list.get(node)
                    matrix[row][col] = neighborsEdgeCost[edgeIndex]
                    edgeIndex += 1

                edgeIndex = 0

        return matrix

    # Print given adjacency matrix
    # param_1: matrix: np.ndarray
    @classmethod
    def printAdjMatrix(self, matrix: np.ndarray):
        print("  ", end=" ")
        for i in range(self.letters.size):
            print(f"{self.letters[i]} ", end=" ")

        print()
        for rows in range(12):
            print(f"{self.letters[rows]}: ", end="")
            for cols in range(12):
                if matrix[rows][cols] < 10:
                    print(f"{matrix[rows,cols]} ", end=" ")
                else:
                    print(f"{matrix[rows,cols]}", end=" ")

            print()

        return
