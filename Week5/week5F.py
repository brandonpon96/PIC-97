#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.c_d = 50
        self.c_x = 0
        self.c_y = 0
        self.color = QtGui.QColor(255,0,0)
        self.canMove = False
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Week5W')

        self.choose = QtGui.QColorDialog()
        #self.choose.move(0, 200)
        #self.fontColor = QtGui.QAction('Font bg Color', self)
        self.choose.colorSelected.connect(self.color_picker)
        #self.choose.addAction(self.fontColor)
        self.choose.setVisible(False)
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def color_picker(self):
        self.color = self.choose.selectedColor()
        
    def drawRectangles(self, qp):
      
        color = QtGui.QColor(255, 255, 255)
        qp.setPen(color)

        qp.setBrush(color)
        qp.drawRect(0, 0, 600, 400)

        qp.setBrush(self.color)
        qp.drawRect(self.c_x,self.c_y,self.c_d,self.c_d)

    def inBounds(self, x, y):
    	if x > self.c_x and x < self.c_x + self.c_d and y > self.c_y and y < self.c_y + self.c_d:
    		return True

    def mouseDoubleClickEvent(self, QMouseEvent):
        x = QMouseEvent.pos().x()
        y = QMouseEvent.pos().y()
        if self.inBounds(x, y):
    	   self.choose.setVisible(True)

    def mousePressEvent(self, QMouseEvent):
    	x = QMouseEvent.pos().x()
    	y = QMouseEvent.pos().y()
    	self.diff_x = x - self.c_x
    	self.diff_y = y - self.c_y
    	if self.inBounds(x, y):
    		self.canMove = True

    def mouseReleaseEvent(self, QMouseEvent):
    	self.canMove = False


    def mouseMoveEvent(self,QMouseEvent):
    	x = QMouseEvent.pos().x()
    	y = QMouseEvent.pos().y()
    	if self.canMove:
    		self.c_x = x - self.diff_x
    		self.c_y = y - self.diff_y
    		self.update()


    def update(self):
    	super(Window,self).update()
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()