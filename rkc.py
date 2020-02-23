import math

#region Class Declaration

class char():
    def __str__(self):
        return self.value

class Side():
    def __init__(self):
        self.UpLeftCorner = char()
        self.UpEdge = char()
        self.UpRightCorner = char()
        self.LeftEdge = char()
        self.Center = char()
        self.RightEdge = char()
        self.DownLeftCorner = char()
        self.DownEdge = char()
        self.DownRightCorner = char()
        self.Face = [[self.UpLeftCorner, self.UpEdge, self.UpRightCorner], [self.LeftEdge, self.Center, self.RightEdge], [self.DownLeftCorner, self.DownEdge, self.DownRightCorner]]
        self.Up = [self.UpLeftCorner, self.UpEdge, self.UpRightCorner]
        self.Right = [self.UpRightCorner, self.RightEdge, self.DownRightCorner]
        self.Down = [self.DownRightCorner, self.DownEdge, self.DownLeftCorner]
        self.Left = [self.DownLeftCorner, self.LeftEdge, self.UpLeftCorner]

    def SetAdjacents(self, adjacents):
        self.Adjacents = adjacents

    def SetText(self, text):
        self.UpLeftCorner.value = text[0]
        self.UpEdge.value = text[1]
        self.UpRightCorner.value = text[2]
        self.LeftEdge.value = text[3]
        self.Center.value = text[4]
        self.RightEdge.value = text[5]
        self.DownLeftCorner.value = text[6]
        self.DownEdge.value = text[7]
        self.DownRightCorner.value = text[8]

    def Turn(self, clockwise):
        buffer = []
        opo = [[0 for x in range(3)] for x in range(3)]
        for x in range(3):
            for y in range(3):
                opo[y][x] = self.Face[x][y].value

        if clockwise:

            for x in range(3):
                aux = opo[x][0]
                opo[x][0] = opo[x][2]
                opo[x][2] = aux


            buffer.append([x.value for x in self.Adjacents[len(self.Adjacents) - 1]])
            for x in self.Adjacents[:len(self.Adjacents) - 1]:
                buffer.append([y.value for y in x])
        else:

            for x in range(3):
                aux = opo[0][x]
                opo[0][x] = opo[2][x]
                opo[2][x] = aux

            for x in self.Adjacents[1:]:
                buffer.append([y.value for y in x])
            buffer.append([x.value for x in self.Adjacents[0]])

        for x in range(3):
            for y in range(3):
                self.Face[x][y].value = opo[x][y]
        for x in range(4):
            for y in range(3):
                self.Adjacents[x][y].value = buffer[x][y]

    def __str__(self):
        return f'{self.UpLeftCorner} {self.UpEdge} {self.UpRightCorner}\n{self.LeftEdge} {self.Center} {self.RightEdge}\n{self.DownLeftCorner} {self.DownEdge} {self.DownRightCorner}'

#endregion

#region Side Registration

white = Side()
orange = Side()
green = Side()
red = Side()
yellow = Side()
blue = Side()

white.SetAdjacents([blue.Down, red.Up, green.Up, orange.Up])
orange.SetAdjacents([white.Left, green.Left, yellow.Left, blue.Left])
green.SetAdjacents([white.Down, red.Left, yellow.Up, orange.Right])
red.SetAdjacents([white.Right, blue.Right, yellow.Right, green.Right])
yellow.SetAdjacents([green.Down, red.Down, blue.Up, orange.Down])
blue.SetAdjacents([yellow.Down, red.Right, white.Up, orange.Left])

Sides = {'U':white, 'L':orange, 'F':green, 'R':red, 'D':yellow, 'B':blue}

#endregion

output = ''
msg = input('')

msg += ((math.ceil(len(msg) / 54) * 54) - len(msg)) * ' '
msg = [msg[x:x+54] for x in range(0, len(msg), 54)]
msg = [[coiso[x:x+9] for x in range(0, len(coiso), 9)] for coiso in msg]

scramble = input('')
scramble += ' '
scramble = scramble.split(' ')
scramble = scramble[:len(scramble) - 1]

for x in msg:
    for y in range(len(x)):
        list(Sides.values())[y].SetText(x[y])

    for y in scramble:
        if len(y) == 1:
            Sides[y].Turn(True)
        elif y[1] == '\'':
            Sides[y[0]].Turn(False)
        else:
            for z in range(2):
                Sides[y[0]].Turn(True)

    for a in Sides.values():
        for b in a.Face:
            for c in b:
                output += c.value

print(output)
