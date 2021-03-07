
class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value

class Automaton:
    def __init__(self, size, distance, limit, initialValues):
        self.start = 1
        self.size = size
        self.distance = distance
        self.limit = limit
        self.grid = []
        self.fillGrid(initialValues)
    
    def calcValue(self, cell):
        sumValue = 0
        for cellGrid in self.grid:
            d = self.getCellsDistance(cell, cellGrid)
            if d <= self.distance:
                sumValue += cellGrid.value
        return sumValue % self.limit

    def getCellsDistance(self, cellOne, cellTwo):
        return min(
            abs(cellOne.position - cellTwo.position), 
            self.size - abs(cellOne.position - cellTwo.position)
            )

    def fillGrid(self, initialValues):
        self.grid = [Cell(position=i, value=initialValues[i - self.start]) for i in range(self.start, self.size+self.start)]

    def nextStep(self):
        newGrid = []
        for cell in self.grid:
            value=self.calcValue(cell)
            newGrid.append(Cell(position=cell.position, value=value))
        self.grid = newGrid

    def __str__(self):
        gridParsed = [str(cell.value) for cell in self.grid]
        return " ".join(gridParsed)

class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        map(self.automaton.nextStep(), range(self.executions))

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
        self.clearOutput()

    def clearOutput(self):
        open(self.outFile, "w").close()

    def fillTestCases(self, cellSplit):
        args = cellSplit[0].split(" ")
        values = cellSplit[1].split(" ")
        args = [ int(i) for i in args ]
        values = [ int(i) for i in values ]
        self.testCase = TestCase(n=args[0], m=args[1], d=args[2], k=args[3], i=values)      

    def readInput(self):
        f = open(self.inFile, "r")
        cellIn = f.read()
        cellSplit = cellIn.splitlines()
        self.fillTestCases(cellSplit)
        f.close()
        

    def writeOutput(self, output):
        f = open(self.outFile, "a")
        f.write("%s\n" % output)
        f.close()


def main():
    reader = Reader(inFile="cell.in", outFile="cell.out")
    reader.readInput() 
    test = reader.testCase
    automaton = Automaton(size=test.n, limit=test.m, distance=test.d, initialValues=test.i)
    engine = Engine(executions=test.k, automaton=automaton)
    engine.run()
    reader.writeOutput(str(automaton))

main()
