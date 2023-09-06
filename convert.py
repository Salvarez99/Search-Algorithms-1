import numpy as np


class convert:
    letters = np.array(["S", "A", "B", "C", "D", 'E','F', 'H', 'P', 'Q', 'R', 'G'])
    vertices = {'S': 0,
                'A': 1,
                'B': 2,
                'C': 3,
                'D': 4,
                'E': 5,
                'F': 6,
                'H': 7,
                'P': 8,
                'Q': 9,
                'R': 10,
                'G': 11}

    matrix: np.ndarray
    vertex_list: dict[str, list[str]]

    @classmethod
    def convertListToMatrixUW(self, matrix: np.ndarray, vertex_list: dict[str, list[str]]):
        for key, values in vertex_list.items():
            if key in self.vertices:
                row = self.vertices.get(key)
                for value in values:
                    col = self.vertices.get(value)
                    matrix[row][col] = 1

        return matrix

    @classmethod
    def printAdjMatrix(self, matrix: np.ndarray):
        print("   ", end=" ")
        for i in range(self.letters.size):
            print(f"{self.letters[i]}", end=" ")

        print("\n")
        for rows in range(12):
            print(f"{self.letters[rows]}: ", end=" ")
            for cols in range(12):
                print(f"{matrix[rows,cols]}", end=" ")
            print("\n")

        return
