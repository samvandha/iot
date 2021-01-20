from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtCore import QDate, QTime, Qt, pyqtSlot, QTimer
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QRadioButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
import os
import time
import cv2 as cv
import numpy as np
import datetime
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import *
from tinydb import TinyDB, Query
x = datetime.datetime.now()
print(type(x.strftime("%X")))
global button_number
button_number = 0
running_process = []
targets = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
attention_list = []
number1 = 0
class Window(QMainWindow):
   global button_number
   def __init__(self):
      super().__init__()
      title = "Start Station in PyQt5"
      top = 40
      left = 40
      width = 1000
      height = 700
      self.setWindowTitle('TCCS IOT DATABASE')
      self.setGeometry(top, left, width, height)
      self.createTable()
      self.MyUI()
      
      self.show()

   def createTable(self):
      global number1
      global tableWidget
      tableWidget = QTableWidget(self)
      tableWidget.setRowCount(6)
      tableWidget.setColumnCount(2)
      k = 0
      
      number1 += 1
      global attention_list
      db= TinyDB('TSSC_inventory.json')
      attention_list = []
      for i in db:
         tableWidget.setItem(k,0, QTableWidgetItem(str(i['Product'])))
         tableWidget.setItem(k,1, QTableWidgetItem(str(i['Number'])))
         #tableWidget.setItem(0,0, QTableWidgetItem(str(number1)))
         if i['Number'] < 10:
            attention_list.append(i['Product'])
         k += 1
         #print(i['Product'])
      w = self
      label13 = QLabel(w)
      label13.setText(str(attention_list))
      label13.resize(500,40)
      label13.move(600, 620)
      label13.setFont(QFont('Arial', 15))
      label13.setStyleSheet("color: red")
      tableWidget.move(600,200)
      tableWidget.resize(350,350)
      tableWidget.horizontalHeader().setStretchLastSection(True) 
      tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
      tableWidget.verticalHeader().setStretchLastSection(True) 
      tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
      
      db.close()
      
   def MyUI(self):
      global attention_list
      w = self
      label_date = QLabel(self)
      x = datetime.datetime.now()
      date_today = x.strftime("%x") 
      label_date.setText("Date:" + date_today)
      label_date.resize(230,30)
      label_date.move(780, 35)
      label_date.setFont(QFont('Arial', 20))
      label_date.setStyleSheet("color: red")
      label = QLabel(w)
      label.setText("<b>DATABASE FOR PRODUCTS</b>")
      label.resize(500,40)
      label.move(290, 30)
      label.setFont(QFont('Arial', 25))
      label1 = QLabel(w)
      label1.setText("<b>Parts Required</b>")
      label1.resize(500,40)
      label1.move(50, 120)
      label1.setFont(QFont('Arial', 25))
      label1.setStyleSheet("color: green")
      label11 = QLabel(w)
      label11.setText("<b>Inventory</b>")
      label11.resize(500,40)
      label11.move(600, 150)
      label11.setFont(QFont('Arial', 25))
      label11.setStyleSheet("color: green")
      label11 = QLabel(w)
      label11.setText("<b>ATTENTION less units </b>")
      label11.resize(500,40)
      label11.move(600, 580)
      label11.setFont(QFont('Arial', 25))
      label11.setStyleSheet("color: red")
      label13 = QLabel(w)
      label13.setText(str(attention_list))
      label13.resize(500,40)
      label13.move(600, 620)
      label13.setFont(QFont('Arial', 15))
      label13.setStyleSheet("color: red")
      b1 = QLabel(w)
      b1.setText("Product 1- Sheet 6 inch, Bracket")
      b1.resize(550,30)
      b1.move(50, 170)
      b1.setFont(QFont('Arial', 20))
      b1.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
   
      b2 = QLabel(w)
      b2.setText("Product 2- Sheet 8 inch, T joint")
      b2.resize(550,30)
      b2.move(50, 240)
      b2.setFont(QFont('Arial', 20))
      b2.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      
      b3 = QLabel(w)
      b3.setText("Product 3- Bracket, T joint")
      b3.resize(550,30)
      b3.move(50, 310)
      b3.setFont(QFont('Arial', 20))
      b3.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b4 = QLabel(w)
      b4.setText("Product 4- Rod, Sheet 6 inch")
      b4.resize(550,30)
      b4.move(50, 380)
      b4.setFont(QFont('Arial', 20))
      b4.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b5 = QLabel(w)
      b5.setText("Product 5- Sheet 8 inch, Rod, Sheet 6 inch")
      b5.resize(550,30)
      b5.move(50, 450)
      b5.setFont(QFont('Arial', 20))
      b5.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b6 = QLabel(w)
      b6.setText("Product 6- SS304 10 inch, Rod")
      b6.resize(550,30)
      b6.move(50, 520)
      b6.setFont(QFont('Arial', 20))
      b6.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b7 = QLabel(w)
      b7.setText("Product 7- Sheet 8 inch, SS304 10 inch")
      b7.resize(550,30)
      b7.move(50, 590)
      b7.setFont(QFont('Arial', 20))
      b7.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      button61 = QPushButton(w)
      button61.setText("Add to Inventory")
      button61.setFont(QFont('Arial', 15))
      button61.resize(200,70)
      button61.move(30, 20)
      button61.setStyleSheet("background-color: #0c940c");

      x = datetime.datetime.now()
      global label_time
      label_time = QLabel(self)
      time_now = x.strftime("%X")
      label_time.setText(time_now)
      label_time.resize(300,40)
      label_time.move(780, 80)
      label_time.setFont(QFont('Arial', 20))
      label_time.setStyleSheet("color: red")
      timer = QTimer(self)
      timer.timeout.connect(self.update_time)
      timer.start(1000)
   def update_time(self):
      global number1
      x = datetime.datetime.now()
      time_now = x.strftime("%X")
      label_time.setText(time_now)
      db= TinyDB('TSSC_inventory.json')
      attention_list = []
      k = 0
      for i in db:
         #print("Hi", number1)
         tableWidget.setItem(k,0, QTableWidgetItem(str(i['Product'])))
         tableWidget.setItem(k,1, QTableWidgetItem(str(i['Number'])))
         #tableWidget.setItem(0,0, QTableWidgetItem(str(number1)))
         if i['Number'] < 10:
            attention_list.append(i['Product'])
         k += 1
      db.close()
      #self.createTable()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
