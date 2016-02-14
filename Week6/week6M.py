#run python /Users/brandon/anaconda2/lib/python2.7/site-packages/PyQt4/uic/pyuic.py design.ui > design_file.py to update qt designer file

from PyQt4 import QtCore, QtGui, uic
from design_file import Ui_MainWindow
import csv
import sys

#qtCreatorFile = "design.ui"

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)



class Canvas(QtGui.QWidget):
	def __init__(self, parent = None):
		super(Canvas, self).__init__()
		self.c_d = 10
		self.c_x = 0
		self.c_y = 0

	def action(self, x, y):
		self.c_x = x
		self.c_y = y
		self.update()

	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self, qp):
		width = self.width()
		height = self.height()
		color = QtGui.QColor(0, 0, 0)
		qp.setPen(color)

		qp.setBrush(QtGui.QColor(255, 255, 255))
		qp.drawRect(0,0, width, height)

		qp.setBrush(QtGui.QColor(0,0,0))
		qp.drawEllipse(self.c_x,self.c_y,self.c_d,self.c_d)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.list = []
		self.actionOpen.triggered.connect(self.openDialog)
		self.Play_button.clicked.connect(self.pressPlay)
		self.Stop_button.clicked.connect(self.pressStop)
		self.play_bool = False
		self.tickpos = 0
		self.refresh = 10

		self.Slider.valueChanged.connect(self.sync)
		self.Slider.sliderPressed.connect(self.pressSlider)
		self.Slider.sliderReleased.connect(self.releaseSlider)
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.animate)

	def pressSlider(self):
		self.timer.stop()

	def releaseSlider(self):
		if self.play_bool:
			self.timer.start(self.refresh)
		self.tickpos = self.Slider.value()

	def sync(self, val):
		self.widget.action(self.list[val][0],self.list[val][1])

	def openDialog(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
		with open(fname, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				row[0] = int(row[0])
				row[1] = int(row[1])
				self.list.append(row)

		self.play_length = len(self.list)
		self.Slider.setMaximum(self.play_length-1)
		self.widget.action(self.list[0][0],self.list[0][1])

	def pressPlay(self):
		self.play_bool = not self.play_bool
		if self.play_bool:
			self.Play_button.setText("Pause")
			self.timer.start(self.refresh)
		else:
			self.Play_button.setText("Play ")
			self.timer.stop()

	def pressStop(self):
		self.play_bool = False
		self.tickpos = 0
		self.timer.stop()
		self.Play_button.setText("Play ")
		self.Slider.setValue(self.tickpos)

	def animate(self):
		if self.tickpos < self.play_length:
			self.tickpos = self.tickpos + 1
			self.Slider.setValue(self.tickpos)
		else:
			self.play_bool = False
			self.Play_button.setText("Play ")
			self.timer.stop()
		self.update()

	def update(self):
		super(MyApp,self).update()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())