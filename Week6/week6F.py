#run python /Users/brandon/anaconda2/lib/python2.7/site-packages/PyQt4/uic/pyuic.py design.ui > design_file.py to update qt designer file

from PyQt4 import QtCore, QtGui, uic
from designF_file import Ui_MainWindow
from sympy import *
import sys, re

#qtCreatorFile = "design.ui"

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		
		self.input.returnPressed.connect(self.enter_pressed)
		self.inputText = ""

	def plain_math(self, word):
		for l in word:
			if l.isalpha():
				return False
		return True

	def enter_pressed(self):
		self.inputText = str(self.input.text())
		if self.plain_math(self.inputText):
			self.result.setText(str(sympify(self.inputText)))
			return
		if self.inputText == self.inputText.replace('^', '**'):
			carrot = False
		else:
			carrot = True
			self.inputText = self.inputText.replace('^', '**')
		self.inputText = self.inputText.replace('differentiate', 'diff')
		self.inputText = self.inputText.replace('derivative', 'diff')
		if self.inputText.find('integr') < 0:
			self.inputText = self.inputText.replace('int', 'integrate')
		self.inputText = self.inputText.replace('integral', 'integrate')
		self.inputText = self.inputText.replace('solution', 'solve')
		if self.inputText.find('solve') < 0:
			self.inputText = self.inputText.replace('sol', 'solve')
		if self.inputText.find('=') > 0:
			regex = r"(.*)=(.*)(,.*)"
			self.inputText = re.sub(regex, r"\1-(\2)\3", self.inputText)
		x, t, z, nu = symbols('x t z nu')
		y = Function('y')
		self.output = eval(self.inputText)
		outputText = str(self.output)
		if carrot:
			outputText = outputText.replace('**', '^')
		self.result.setText(outputText)




if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())