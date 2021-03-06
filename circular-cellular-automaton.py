
class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def __str__(self):
        return "position=" + str(self.position) + "value=" + str(self.value)

class Automaton:
    def __init__(self, size, distance, limit, initialValues):
        self.start = 1
        self.size = size
        self.distance = distance
        self.limit = limit
        self.grid = []
        self.fillGrid(initialValues)
    
    def getNeighbors(self, cell):
        neighbors = []
        for cellGrid in self.grid:
            d = self.getCellsDistance(cell, cellGrid)
            if d <= self.distance:
                neighbors.append(cellGrid)
        return neighbors

    def calcValue(self, neighbors):
        sumValue = 0
        for cell in neighbors:
            sumValue += cell.value
        return sumValue % self.limit

    def getCellsDistance(self, cellOne, cellTwo):
        return min(
            abs(cellOne.position - cellTwo.position), 
            self.size - abs(cellOne.position - cellTwo.position)
            )

    def fillGrid(self, initialValues):
        for i in range(self.start, self.size+self.start):
            cell = Cell(position=i, value=initialValues[i - self.start])
            self.grid.append(cell)

    def nextStep(self):
        newGrid = []
        for cell in self.grid:
            neighbors = self.getNeighbors(cell)
            value=self.calcValue(neighbors)
            newGrid.append(Cell(position=cell.position, value=value))
        self.grid = newGrid

    def __str__(self):
        strAutomaton = ""
        for index, cell in enumerate(self.grid):
            if index != 0:
                strAutomaton += " "
            strAutomaton += str(cell.value) 
            
        return strAutomaton

class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        for i in range(self.executions):
            self.automaton.nextStep()

class TestCase:
    def __init__(self, n, m, d, k, i):
        self.n = n
        self.m = m
        self.d = d
        self.k = k
        self.i = i

class Reader:
    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile
        self.testCases = []
        self.clearOutput()

    def clearOutput(self):
        open(self.outFile, "w").close()

    def fillTestCases(self, cellSplit):
        for i in range(0, len(cellSplit), 2):
            args = cellSplit[i].split(" ")
            values = cellSplit[i+1].split(" ")
            args = [ int(i) for i in args ]
            values = [ int(i) for i in values ]
            self.testCases.append(TestCase(n=args[0], m=args[1], d=args[2], k=args[3], i=values))        

    def readInput(self):
        f = open(self.inFile, "r")
        cellIn = f.read()
        cellSplit = cellIn.splitlines()
        self.fillTestCases(cellSplit)
        f.close()
        

    def writeOutput(self, output):
        f = open(self.outFile, "a")
        f.write(output)
        f.write("\n")
        f.close()


def main():
    reader = Reader(inFile="cell.in", outFile="cell.out")
    reader.readInput() 
    for index, test in enumerate(reader.testCases):
        automaton = Automaton(size=test.n, limit=test.m, distance=test.d, initialValues=test.i)
        engine = Engine(executions=test.k, automaton=automaton)
        engine.run()
        reader.writeOutput(str(automaton))

main()
