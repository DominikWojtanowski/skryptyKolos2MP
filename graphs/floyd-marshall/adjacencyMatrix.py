import random


class AdjacencyMatrix:
    def __init__(self, numOfVertices):
        self.graph = [[0 for _ in range(numOfVertices)]
                      for _ in range(numOfVertices)]
        self.numOfVertices = numOfVertices

    def assignTwoWayConnectedGraph(self, density=0.5):
        """Generuje losowy graf NIESKIEROWANY (dwukierunkowy)."""
        # Czyścimy graf na wypadek ponownego wywołania funkcji

        for i in range(self.numOfVertices):
            # Iterujemy tylko po "górnym trójkącie" macierzy (j zaczyna się od i + 1)
            for j in range(i + 1, self.numOfVertices):
                if random.random() < density:
                    self.graph[i][j] = 1
                    # LUSTRZANE ODBICIE - krawędź działa w obie strony
                    self.graph[j][i] = 1

    def assignOneWayConnectedGraph(self, density=0.5):
        """Generuje losowy graf SKIEROWANY (jednokierunkowy)."""
        # Czyścimy graf na wypadek ponownego wywołania funkcji

        for i in range(self.numOfVertices):
            for j in range(self.numOfVertices):
                # i != j zapobiega tworzeniu "pętli własnych" (wierzchołek nie wskazuje sam na siebie)
                if i != j and random.random() < density:
                    self.graph[i][j] = 1

    def printGraph(self):
        """Prosta metoda pomocnicza, żebyś mógł zobaczyć swoją macierz w konsoli."""
        for row in self.graph:
            print(row)
