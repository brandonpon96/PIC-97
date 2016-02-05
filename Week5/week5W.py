#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.c_d = 30
        self.c_x = 0
        self.c_y = 0
        self.cv_x = 10
        self.cv_y = 10
        self.dir_x = 1
        self.dir_y = 1
        self.timer = QtCore.QTimer()
    	self.timer.timeout.connect(self.animate)
    	self.timer.start(30)
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Week5W')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        color = QtGui.QColor(255, 255, 255)
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, 600, 400)

        qp.setBrush(QtGui.QColor(255,0,0))
        qp.drawEllipse(self.c_x,self.c_y,self.c_d,self.c_d)

    def animate(self):
    	if self.c_x > 600 - self.c_d or self.c_x < 0:
    		self.dir_x = self.dir_x * -1
    	if self.c_y > 400 - self.c_d or self.c_y < 0:
    		self.dir_y = self.dir_y * -1
    	self.c_x = self.c_x + self.cv_x * self.dir_x
    	self.c_y = self.c_y + self.cv_y * self.dir_y
    	self.update()

    def update(self):
    	super(Window,self).update()
              
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()