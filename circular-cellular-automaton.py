import copy

# Classe que representa uma célula do autômato celular
class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def __str__(self):
        return "position=" + str(self.position) + "value=" + str(self.value)

# n = size  
# m = limit
# d = distance
# Classe que representa o autômato celular
class Automaton:
    def __init__(self, size, distance, limit, initialValues):
        self.start = 1
        self.size = size
        self.distance = distance
        self.limit = limit
        self.grid = []
        self.fillGrid(initialValues)
    
    # retorna todas as células com distancia >= d para a celula de referencia
    def getNeighbors(self, cell):
        neighbors = []
        for cellGrid in self.grid:
            d = self.getCellsDistance(cell, cellGrid)
            if d <= self.distance:
                neighbors.append(cellGrid)
        return neighbors

    # calcula o novo valor da celula com base na
    # soma dos valores dos vizinhos módulo ordem da célula
    def calcValue(self, neighbors):
        sumValue = 0
        for cell in neighbors:
            sumValue += cell.value
        return sumValue % self.limit

    # calcula a distancia entre duas células
    def getCellsDistance(self, cellOne, cellTwo):
        return min(
            abs(cellOne.position - cellTwo.position), 
            self.size - abs(cellOne.position - cellTwo.position)
            )

    # preenche a lista circular de células
    def fillGrid(self, initialValues):
        for i in range(self.start, self.size+self.start):
            cell = Cell(position=i, value=initialValues[i - self.start])
            self.grid.append(cell)

    # executa os calculos de distância entre as célular e atualiza a lista
    def nextStep(self):
        newGrid = []
        for cell in self.grid:
            neighbors = self.getNeighbors(cell)
            value=self.calcValue(neighbors)
            newGrid.append(Cell(position=cell.position, value=value))
        self.grid = newGrid

    def __str__(self):
        strAutomaton = "[ "
        for cell in self.grid:
            strAutomaton += str(cell.value) + " "
        strAutomaton += "]"
        return strAutomaton



# k = executions
# classe que representa o motor que executa as etapas do autômato
class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        for i in range(self.executions):
            self.automaton.nextStep()
            # print("Step " + str(i + 1) + ": " + str(self.automaton))


def main():
    n = 5
    m = 3
    d = 1
    k = 10
    i = [1, 2, 2, 1, 2]

    automaton = Automaton(size=n, limit=m, distance=d, initialValues=i)
    engine = Engine(executions=k, automaton=automaton)

    engine.run()
    print(automaton)

main()
        


