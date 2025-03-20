class Map():
    def __init__(self):
        self.matrix = [[0,0,0], [0,0,0], [0,0,0]]
    def add(self, figure, position):
        match position:
            case 1:
                self.matrix[0][0] = figure
            case 2:
                self.matrix[0][1] = figure
            case 3:
                self.matrix[0][2] = figure
            case 4:
                self.matrix[1][0] = figure
            case 5:
                self.matrix[1][1] = figure
            case 6:
                self.matrix[1][2] = figure
            case 7:
                self.matrix[2][0] = figure
            case 8:
                self.matrix[2][1] = figure
            case 9:
                self.matrix[2][2] = figure
    def remove(self, position):
        match position:
            case 1:
                self.matrix[0][0] = 0
            case 2:
                self.matrix[0][1] = 0
            case 3:
                self.matrix[0][2] = 0
            case 4:
                self.matrix[1][0] = 0
            case 5:
                self.matrix[1][1] = 0
            case 6:
                self.matrix[1][2] = 0
            case 7:
                self.matrix[2][0] = 0
            case 8:
                self.matrix[2][1] = 0
            case 9:
                self.matrix[2][2] = 0
    def check(self):
        for i in range(3):
            if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] != 0:
                return self.matrix[i][0]
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] != 0:
                return self.matrix[0][i]
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != 0:
            return self.matrix[0][0]
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != 0:
            return self.matrix[0][2]
        return 0