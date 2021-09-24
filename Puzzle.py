import sys
import random
import numpy as np
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from functools import partial
        
class PuzzleBlock(QtWidgets.QLabel):
    
    def __init__(self, window, index, src):
        super().__init__(window)
        
        self.index = index
        self.src = src
        self.posx = 2000
        self.posy = 2000
        self.isPut = False
        
        self.setPixmap(QtGui.QPixmap(src))
        self.move(2000, 2000)
        
class SwitchButton(QtWidgets.QPushButton):
    
    def __init__(self, window, puzzleBlocks):
        super().__init__('', window)
    
        startBlock = puzzleBlocks[random.randint(0, 24)]
        self.setIcon(QIcon(startBlock.src))
        self.setIconSize(QSize( 93, 95))
        self.setStyleSheet("QPushButton{background: transparent;}")
        self.move(2000, 2000)
        
        self.currentBlockIndex = startBlock.index

class Window(QWidget):
    
    def __init__( self, windowPositionX, windowPositionY, windowWidth, windowHeight, title):
        super().__init__()
      
        self.setGeometry( windowPositionX, windowPositionY, windowWidth, windowHeight)
        self.setWindowTitle( title)
        
        self.initUI( windowWidth, windowHeight)
        
        self.show()
        
    def initUI( self, windowWidth, windowHeight):
        background = QtWidgets.QLabel( self)
        background.setPixmap(QtGui.QPixmap('imgs/background.jpg'))
        title = QtWidgets.QLabel( self)
        title.setPixmap(QtGui.QPixmap('imgs/title.png'))
        title.move( windowWidth / 4, windowHeight / 9)
        
        _18731 = QtWidgets.QLabel( self)
        _18731.setPixmap(QtGui.QPixmap('imgs/18731.png'))
        
        # exit button
        exitButton = QtWidgets.QPushButton('', self)
        exitButton.setIcon(QIcon('imgs/exit.png'))        
        exitButton.setIconSize(QSize(400, 300))
        exitButton.setStyleSheet("QPushButton{background: transparent;}");
        exitButton.move( windowWidth / 2, windowHeight / 2)
        exitButton.clicked.connect(self.onExitButtonClicked)
        
        # play button
        playButton = QtWidgets.QPushButton('', self)
        playButton.setIcon(QIcon('imgs/play.png'))        
        playButton.setStyleSheet("QPushButton{background: transparent;}");
        playButton.move( windowWidth / 10, windowHeight / 2)
        playButton.setIconSize(QSize(400, 300))
        
        widgetsToHide = [ title, _18731, playButton, exitButton]
        
        # widgety do ekranu gry
        
        grid = QtWidgets.QLabel( self)
        grid.setPixmap(QtGui.QPixmap('imgs/grid.png'))
        grid.move(2000, 2000)
        
        
        panel = QtWidgets.QLabel(self)
        panel.setPixmap(QtGui.QPixmap('imgs/panel.png'))
        panel.move(2000, 2000)
        
        panel2 = QtWidgets.QLabel(self)
        panel2.setPixmap(QtGui.QPixmap('imgs/panel.png'))
        panel2.move(2000, 2000)
        
        _12345h = QtWidgets.QLabel(self)
        _12345h.setPixmap(QtGui.QPixmap('imgs/12345h.png'))
        _12345h.move(2000, 2000)
        
        _12345v = QtWidgets.QLabel(self)
        _12345v.setPixmap(QtGui.QPixmap('imgs/12345v.png'))
        _12345v.move(2000, 2000)
        
        inputsText = QtWidgets.QLabel(self)
        inputsText.setPixmap(QtGui.QPixmap('imgs/inputs.png'))
        inputsText.move(2000, 2000)
        
        inputX = QtWidgets.QLineEdit(self)  # X
        inputY = QtWidgets.QLineEdit(self)  # Y
        inputX.move(2000,2000)
        inputY.move(2000,2000)
        
        blockText = QtWidgets.QLabel(self)
        blockText.setPixmap(QtGui.QPixmap('imgs/blocktext.png'))
        blockText.move(2000, 2000)
        
        gridStartX =  windowWidth / 2.1
        gridStartY = windowHeight / 9
        
        wellDone = QtWidgets.QLabel(self)
        wellDone.setPixmap(QtGui.QPixmap('imgs/welldone.png'))
        wellDone.move( 2000, 2000)
        
        puzzleBlocks = [ 
                         PuzzleBlock( self, 1, 'imgs/daschund/1.png'),
                         PuzzleBlock( self, 2, 'imgs/daschund/2.png'),
                         PuzzleBlock( self, 3, 'imgs/daschund/3.png'),
                         PuzzleBlock( self, 4, 'imgs/daschund/4.png'),
                         PuzzleBlock( self, 5, 'imgs/daschund/5.png'),
                         PuzzleBlock( self, 6, 'imgs/daschund/6.png'),
                         PuzzleBlock( self, 7, 'imgs/daschund/7.png'),
                         PuzzleBlock( self, 8, 'imgs/daschund/8.png'),
                         PuzzleBlock( self, 9, 'imgs/daschund/9.png'),
                         PuzzleBlock( self, 10, 'imgs/daschund/10.png'),
                         PuzzleBlock( self, 11, 'imgs/daschund/11.png'),
                         PuzzleBlock( self, 12, 'imgs/daschund/12.png'),
                         PuzzleBlock( self, 13, 'imgs/daschund/13.png'),
                         PuzzleBlock( self, 14, 'imgs/daschund/14.png'),
                         PuzzleBlock( self, 15, 'imgs/daschund/15.png'),
                         PuzzleBlock( self, 16, 'imgs/daschund/16.png'),
                         PuzzleBlock( self, 17, 'imgs/daschund/17.png'),
                         PuzzleBlock( self, 18, 'imgs/daschund/18.png'),
                         PuzzleBlock( self, 19, 'imgs/daschund/19.png'),
                         PuzzleBlock( self, 20, 'imgs/daschund/20.png'),
                         PuzzleBlock( self, 21, 'imgs/daschund/21.png'),
                         PuzzleBlock( self, 22, 'imgs/daschund/22.png'),
                         PuzzleBlock( self, 23, 'imgs/daschund/23.png'),
                         PuzzleBlock( self, 24, 'imgs/daschund/24.png'),
                         PuzzleBlock( self, 25, 'imgs/daschund/25.png') 
                       ]
        
        # do ukladow rownan
        sol_x = [12, 108, 203, 298, 394] # kolejne wspolrzedne x (prawidlowe rozwiazania x rownania)
        
        sol_y = [14, 108, 203, 298, 393] # kolejne wspolrzedne y (prawidlowe rozwiazania y rownania)
        
        x_factors = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        y_factors = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        
        for i in range( 0, 5) :     # losowanie wspolczynnikow
            for j in range ( 0, 5) :
                x_factors[i][j] = random.randint( -100, 100)
                y_factors[i][j] = random.randint( -100, 100)
        
        free_num_x = np.array([  # 5 wektorow x1 * a + x2 * b + x3 * c + x4 * d + x5 * d, z ktorych jest 5 wyrazow wolnych
                sol_x[0] * x_factors[0][0] + sol_x[1] * x_factors[0][1] + sol_x[2] * x_factors[0][2] + sol_x[3] * x_factors[0][3] + sol_x[4] * x_factors[0][4],
                sol_x[0] * x_factors[1][0] + sol_x[1] * x_factors[1][1] + sol_x[2] * x_factors[1][2] + sol_x[3] * x_factors[1][3] + sol_x[4] * x_factors[1][4],
                sol_x[0] * x_factors[2][0] + sol_x[1] * x_factors[2][1] + sol_x[2] * x_factors[2][2] + sol_x[3] * x_factors[2][3] + sol_x[4] * x_factors[2][4],
                sol_x[0] * x_factors[3][0] + sol_x[1] * x_factors[3][1] + sol_x[2] * x_factors[3][2] + sol_x[3] * x_factors[3][3] + sol_x[4] * x_factors[3][4],
                sol_x[0] * x_factors[4][0] + sol_x[1] * x_factors[4][1] + sol_x[2] * x_factors[4][2] + sol_x[3] * x_factors[4][3] + sol_x[4] * x_factors[4][4]
                ])
        
        free_num_y = np.array([
                sol_y[0] * y_factors[0][0] + sol_y[1] * y_factors[0][1] + sol_y[2] * y_factors[0][2] + sol_y[3] * y_factors[0][3] + sol_y[4] * y_factors[0][4],
                sol_y[0] * y_factors[1][0] + sol_y[1] * y_factors[1][1] + sol_y[2] * y_factors[1][2] + sol_y[3] * y_factors[1][3] + sol_y[4] * y_factors[1][4],
                sol_y[0] * y_factors[2][0] + sol_y[1] * y_factors[2][1] + sol_y[2] * y_factors[2][2] + sol_y[3] * y_factors[2][3] + sol_y[4] * y_factors[2][4],
                sol_y[0] * y_factors[3][0] + sol_y[1] * y_factors[3][1] + sol_y[2] * y_factors[3][2] + sol_y[3] * y_factors[3][3] + sol_y[4] * y_factors[3][4],
                sol_y[0] * y_factors[4][0] + sol_y[1] * y_factors[4][1] + sol_y[2] * y_factors[4][2] + sol_y[3] * y_factors[4][3] + sol_y[4] * y_factors[4][4]
                ])
        
        switchButton = SwitchButton( self, puzzleBlocks)
        switchButton.clicked.connect( partial(self.onSwitchButtonClicked, puzzleBlocks))
        
         # play again button
        playAgainButton = QtWidgets.QPushButton('', self)
        playAgainButton.setIcon(QIcon('imgs/playagain.png'))        
        playAgainButton.setIconSize(QSize(180, 40))
        playAgainButton.setStyleSheet("QPushButton{background: transparent;}");
        playAgainButton.move( 2000, 2000)
        
        # small exit button
        smallExitButton = QtWidgets.QPushButton('', self)
        smallExitButton.setIcon(QIcon('imgs/exit2.png'))        
        smallExitButton.setIconSize(QSize(180, 30))
        smallExitButton.setStyleSheet("QPushButton{background: transparent;}");
        smallExitButton.move( 2000, 2000)
        smallExitButton.clicked.connect(self.onExitButtonClicked)
        
        # put button
        putButton = QtWidgets.QPushButton('', self)
        putButton.setIcon(QIcon('imgs/put.png'))        
        putButton.setIconSize(QSize(150, 100))
        putButton.setStyleSheet("QPushButton{background: transparent;}");
        putButton.move( 2000, 2000)
        putButton.clicked.connect( partial(self.onPutButtonClicked, puzzleBlocks, switchButton, inputX, inputY,
                                           gridStartX, gridStartY, wellDone, sol_x, sol_y, x_factors, y_factors,
                                           free_num_x, free_num_y, playAgainButton, smallExitButton))
        
        # remove button
        removeButton = QtWidgets.QPushButton('', self)
        removeButton.setIcon(QIcon('imgs/remove.png'))        
        removeButton.setIconSize(QSize(150, 100))
        removeButton.setStyleSheet("QPushButton{background: transparent;}");
        removeButton.move( 2000, 2000)
        removeButton.clicked.connect( partial(self.onRemoveButtonClicked, puzzleBlocks, inputX, inputY,
                                              gridStartX, gridStartY, switchButton, windowWidth, windowHeight))
        
        
        little = QtWidgets.QLabel(self)
        little.setPixmap(QtGui.QPixmap('imgs/daschund/little.png'))
        little.move( 2000, 2000)
        
        pictureText = QtWidgets.QLabel(self)
        pictureText.setPixmap(QtGui.QPixmap('imgs/picture.png'))
        pictureText.move( 2000, 2000)
        
        widgetsToShow = [grid, panel, inputsText, inputX, inputY, blockText, 
                         putButton, removeButton, switchButton, little, _12345h, _12345v, panel2, pictureText]
        
        
        playButton.clicked.connect(partial( self.onPlayButtonClicked, widgetsToHide))
        playButton.clicked.connect(partial( self.initGame, widgetsToShow, windowWidth, windowHeight))

        playAgainButton.clicked.connect( partial(self.onPlayAgainButtonClicked, puzzleBlocks, widgetsToShow, windowWidth,
                                           windowHeight, wellDone, smallExitButton))
        
        
    def initGame(self, widgets, windowWidth, windowHeight):
        widgets[0].move( windowWidth / 2.1, windowHeight / 9) # grid
        widgets[1].move( windowWidth / 32, windowHeight / 30) # panel height 7
        widgets[2].move( windowWidth / 20, windowHeight / 11) # inputs text
        widgets[3].move( windowWidth / 3.5, windowHeight / 8)   # input x
        widgets[4].move( windowWidth / 3.5, windowHeight / 4.6)  # input y
        widgets[5].move( windowWidth / 20, windowHeight / 2.7) # block text
        widgets[6].move( windowWidth / 20, windowHeight / 2.2) # put button
        widgets[7].move( windowWidth / 3.75, windowHeight / 2.2) # remove button
        widgets[8].move( windowWidth / 3.5, windowHeight / 2.85) # switchButton 
        widgets[9].move( windowWidth / 6, windowHeight / 1.55) # little img
        widgets[10].move( windowWidth / 1.95, windowHeight / 15) # 12345 horizontal
        widgets[11].move( windowWidth / 2.25, windowHeight / 7) # 12345 vertical
        widgets[12].move( windowWidth / 32, windowHeight / 3) # panel2
        widgets[13].move( windowWidth / 7, windowHeight / 1.70) # picture word   
        
        
    def onPlayButtonClicked(self, widgets):
        for widget in widgets:
            widget.move( 2000, 2000)
    
    def onExitButtonClicked(self):
        self.close()
        
    def onSwitchButtonClicked(self, puzzleBlocks):
         sender = self.sender()
         nextBlock = puzzleBlocks[random.randint(0, 24)]         
         
         while nextBlock.isPut:
             nextBlock = puzzleBlocks[random.randint(0, 24)]
         
         sender.setIcon(QIcon(nextBlock.src))
         sender.currentBlockIndex = nextBlock.index
        
        
    def onPutButtonClicked(self, puzzleBlocks, switchButton, inputX, inputY, gridStartX, gridStartY, wellDone,
                           sol_x, sol_y, x_factors, y_factors, free_num_x, free_num_y, playAgainButton, smallExitButton):
        blockToPutList = list( filter( lambda block: block.index == switchButton.currentBlockIndex, puzzleBlocks))
        blockToPut = blockToPutList[0]
        x = int(inputX.text())
        y = int(inputY.text())
        blockToPut.isPut = True
        canMove = True
        inputX.clear()
        inputY.clear()
        posx = 0
        posy = 0
        if x == 1: posx = 12
        elif x == 2: posx = 108
        elif x == 3: posx = 203
        elif x == 4: posx = 298
        elif x == 5: posx = 394
        else:   # jezeli input bez sensu to nie moze sie ruszyc i nie jest oznaczony jako polozony
            blockToPut.isPut = False
            canMove = False
        
        if y == 1: posy = 14
        elif y == 2: posy = 108
        elif y == 3: posy = 203
        elif y == 4: posy = 298
        elif y == 5: posy = 393
        else:   # jezeli input bez sensu to nie moze sie ruszyc i nie jest oznaczony jako polozony
            blockToPut.isPut = False
            canMove = False
        
        nextPosX = posx + gridStartX
        nextPosY = posy + gridStartY
        
        putBlocks = 0
        for block in puzzleBlocks:      # sprawdzenie czy na danej pozycji nie stoi juz jakis inny blok
            if block.posx == nextPosX and block.posy == nextPosY:
                canMove = False
            if block.isPut == True:     # zliczanie polozonych klockow
                putBlocks = putBlocks + 1
        
        if canMove:
            blockToPut.move( nextPosX, nextPosY)
            blockToPut.posx = nextPosX
            blockToPut.posy = nextPosY
            blockToPut.isPut = True
            nextBlock = puzzleBlocks[random.randint(0, 24)] # zmiana switch bloku
            while nextBlock.isPut:
                nextBlock = puzzleBlocks[random.randint(0, 24)]
                if putBlocks == 25: # jezeli wszystkie klocki uzyte to nie szukaj nastepnego nieuzytego
                    break
         
            if putBlocks == 25: # jezeli wszystkie klocki juz uzyte to schowaj przycisk
                switchButton.move(2000, 2000)
                if self.checkIfWin( puzzleBlocks, sol_x, sol_y, x_factors, y_factors, free_num_x, free_num_y, gridStartX, gridStartY):
                    wellDone.move( gridStartX, gridStartY + 500)    # sprawdzenie czy dobrze ulozone
                    playAgainButton.move( gridStartX + 10, gridStartY + 580)
                    smallExitButton.move( gridStartX + 340, gridStartY + 585)
            else:
                switchButton.setIcon(QIcon(nextBlock.src))
                switchButton.currentBlockIndex = nextBlock.index
                
                
    def onRemoveButtonClicked(self, puzzleBlocks, inputX, inputY, gridStartX, gridStartY, switchButton,
                              windowWidth, windowHeight):
        x = int(inputX.text())
        y = int(inputY.text())
        
        inputX.clear()
        inputY.clear()
        posx = 0
        posy = 0
        if x == 1: posx = 12
        elif x == 2: posx = 108
        elif x == 3: posx = 203
        elif x == 4: posx = 298
        elif x == 5: posx = 394
         
            
        
        if y == 1: posy = 14
        elif y == 2: posy = 108
        elif y == 3: posy = 203
        elif y == 4: posy = 298
        elif y == 5: posy = 393
        
        
        posXToRemove = posx + gridStartX
        posYToRemove = posy + gridStartY
        
        blockToRemoveList = list( filter( lambda block: block.posx == posXToRemove and
                                         block.posy == posYToRemove, puzzleBlocks))
        
        if len(blockToRemoveList) > 0:
            blockToRemove = blockToRemoveList[0]
            blockToRemove.move( 2000, 2000)
            blockToRemove.posx = 2000
            blockToRemove.posy = 2000
            blockToRemove.isPut = False
            blocksLeft = 0
            for block in puzzleBlocks:
                if block.isPut == True:
                    blocksLeft = blocksLeft + 1
            if blocksLeft > 0:  # jesli wczesniej wszystkie bloki uzyte ale usunieto to przywroc switchButton
                lastBlockList = list ( filter( lambda block: block.isPut == False, puzzleBlocks))
                lastBlock = lastBlockList[0]
                switchButton.setIcon(QIcon(lastBlock.src))  # ustaw ikone usunietego elementu
                switchButton.currentBlockIndex = lastBlock.index
                switchButton.move(windowWidth / 3.5, windowHeight / 2.75)
    
    def checkIfWin( self, puzzleBlocks, sol_x, sol_y, x_factors, y_factors, free_num_x, free_num_y, 
                       gridStartX, gridStartY):
        win = 1        
        
        # sprawdzenie x - np.linalg.solve(a, b)
        
        guessed_x = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
        
        guessed_y = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
        
        for i in range( 0, 5):  # w tych tablicach sa faktyczne pozycje klockow, niekoniecznie prawidlowe
            for j in range( 0, 5):
                guessed_x[i][j] = puzzleBlocks[i * 5 + j].posx - gridStartX #konieczna poprawka na punkt start siatki
                guessed_y[i][j] = puzzleBlocks[i * 5 + j].posy - gridStartY 
                
        correct_x_sol = np.linalg.solve( x_factors, free_num_x) # METODA NUM 1
        
        for i in range( 0, 5):
            for j in range( 0, 5):
                if int(round(correct_x_sol[j])) != round(guessed_x[i][j]):
                    win = 0
                
        #sprawdzenie y - metoda Gaussa
        R = y_factors
        V = free_num_y
        R.shape = (5, 5)
        V.shape = (1, 5)
        R1 = np.copy(R)
        R2 = np.copy(R)
        R3 = np.copy(R)
        R4 = np.copy(R)
        R5 = np.copy(R)
        R1[:,0] = V[:] # podstawienie V do pierwszej kolumny
        R2[:,1] = V[:] # podstawienie V do drugiej kolumny
        R3[:,2] = V[:] # podstawienie V do trzeciej kolumny
        R4[:,3] = V[:] # podstawienie V do czwartej kolumny
        R5[:,4] = V[:] # podstawienie V do piatej kolumny
        I1 = np.linalg.det(R1) / np.linalg.det(R)   # METODA NUM 2
        I2 = np.linalg.det(R2) / np.linalg.det(R)
        I3 = np.linalg.det(R3) / np.linalg.det(R)
        I4 = np.linalg.det(R4) / np.linalg.det(R)
        I5 = np.linalg.det(R5) / np.linalg.det(R)
        
        correct_y_sol = [I1, I2, I3, I4, I5]

        for i in range( 0, 5):
            for j in range( 0, 5):
                if round(correct_y_sol[j]) != round(guessed_y[j][i]):
                    win = 0

        return win
    
    def onPlayAgainButtonClicked(self, puzzleBlocks, widgetsToShow, windowWidth, windowHeight, wellDone, smallExitButton):
        
        sender = self.sender()
        sender.move( 2000, 2000)
        
        for block in puzzleBlocks:
            block.isPut = False;
            block.posx = 2000;
            block.posy = 2000;
            block.move(block.posx, block.posy)
            
        wellDone.move(2000, 2000)
        smallExitButton.move(2000, 2000)
        
        self.initGame(widgetsToShow, windowWidth, windowHeight)
        
                
if __name__ == '__main__':
    application = QApplication(sys.argv)
    
    winWidth = 1000
    winHeigth = 750
    
    window = Window(300, 50, winWidth, winHeigth, 'Puzzle Project')
    sys.exit(application.exec_())