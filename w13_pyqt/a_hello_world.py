# Použití PyQT5, instalace:
# py -m pip install -U PyQT5 --user

# https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/

# Import sys for handle the 
# exit status of the application.
import sys
  
# Importing required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
  
# To create an instance of QApplication
# sys.argv contains the list of
# command-line argument
app = QApplication(sys.argv)
  
# To create an instance of application GUI
# root is an instance of QWidget,
# it provides all the features to
# create the application's window
root = QWidget()  
  
# adding title to window
root.setWindowTitle('Geeks App') 
  
# to place txt at the coordinates
root.move(60, 15) 
  
# to display text
txt = QLabel('Welcome, Geeks!', parent = root) 
txt.move(60, 15)
  
# Show application's GUI
root.show()
  
# Run application's main loop
sys.exit(app.exec_())