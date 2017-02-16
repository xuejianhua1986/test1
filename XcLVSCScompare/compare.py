#coding=utf-8
#__author__ = 'Jianhua'


import PyQt4

from PyQt4 import QtCore, QtGui
from xlutils.copy import copy
from PyQt4.QtGui import *  
from PyQt4.QtCore import * 
import csv
import xlwt
#import xml.etree.cElementTree as ET
#import datetime
import pandas as pd   #为了使用to_csv
import os
import xlrd
import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')

global new_vscs_address
global old_vscs_address
global out_put_address

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(668, 556)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        
        
        self.newsheetchoose = QtGui.QComboBox(self.centralwidget)
        self.newsheetchoose.setGeometry(QtCore.QRect(510, 20, 121, 22))
        self.newsheetchoose.setObjectName(_fromUtf8("newsheetchoose"))
        
        
        self.newvscs = QtGui.QLabel(self.centralwidget)
        self.newvscs.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.newvscs.setObjectName(_fromUtf8("newvscs"))
        self.newvscsaddress = QtGui.QTextBrowser(self.centralwidget)
        self.newvscsaddress.setGeometry(QtCore.QRect(90, 10, 311, 41))
        self.newvscsaddress.setObjectName(_fromUtf8("newvscsaddress"))
        
        self.newvscschoose = QtGui.QPushButton(self.centralwidget)
        self.newvscschoose.setGeometry(QtCore.QRect(410, 20, 75, 21))
        self.newvscschoose.setAutoRepeatDelay(300)
        self.newvscschoose.setObjectName(_fromUtf8("newvscschoose"))
        self.newvscschoose.clicked.connect(self.choose_new_vscs)
        
        self.oldsheetchoose = QtGui.QComboBox(self.centralwidget)
        self.oldsheetchoose.setGeometry(QtCore.QRect(510, 80, 121, 22))
        self.oldsheetchoose.setObjectName(_fromUtf8("oldsheetchoose"))
        
        
        
        
        self.oldvscsaddress = QtGui.QTextBrowser(self.centralwidget)
        self.oldvscsaddress.setGeometry(QtCore.QRect(90, 70, 311, 41))
        self.oldvscsaddress.setObjectName(_fromUtf8("oldvscsaddress"))
        
        self.oldvscschoose = QtGui.QPushButton(self.centralwidget)
        self.oldvscschoose.setGeometry(QtCore.QRect(410, 80, 75, 21))
        self.oldvscschoose.setAutoRepeatDelay(300)
        self.oldvscschoose.setObjectName(_fromUtf8("oldvscschoose"))
        self.oldvscschoose.clicked.connect(self.choose_old_vscs)
        
        
        
        
        self.oldvscs = QtGui.QLabel(self.centralwidget)
        self.oldvscs.setGeometry(QtCore.QRect(20, 80, 61, 21))
        self.oldvscs.setObjectName(_fromUtf8("oldvscs"))
        
        self.copy = QtGui.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(90, 200, 75, 21))
        self.copy.setAutoRepeatDelay(300)
        self.copy.setObjectName(_fromUtf8("copy"))
        self.copy.clicked.connect(self.vscs_copy)
        
        self.partnumber = QtGui.QPushButton(self.centralwidget)
        self.partnumber.setGeometry(QtCore.QRect(90, 240, 75, 21))
        self.partnumber.setAutoRepeatDelay(300)
        self.partnumber.setObjectName(_fromUtf8("Partnumber"))
        self.partnumber.clicked.connect(self.compare_vscs_part2_partnumber)        
        
        
        self.outputaddress = QtGui.QLabel(self.centralwidget)
        self.outputaddress.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.outputaddress.setObjectName(_fromUtf8("outputaddress"))
        self.outputaddressdisplay = QtGui.QTextBrowser(self.centralwidget)
        self.outputaddressdisplay.setGeometry(QtCore.QRect(90, 130, 311, 41))
        self.outputaddressdisplay.setObjectName(_fromUtf8("outputaddressdisplay"))
        self.outputaddresschoose = QtGui.QPushButton(self.centralwidget)
        self.outputaddresschoose.setGeometry(QtCore.QRect(410, 140, 75, 21))
        self.outputaddresschoose.setAutoRepeatDelay(300)
        self.outputaddresschoose.setObjectName(_fromUtf8("outputaddresschoose"))
        self.outputaddresschoose.clicked.connect(self.output_vscs)
        
        self.comparesheet = QtGui.QPushButton(self.centralwidget)
        self.comparesheet.setGeometry(QtCore.QRect(200, 200, 91, 21))
        self.comparesheet.setAutoRepeatDelay(300)
        self.comparesheet.setObjectName(_fromUtf8("comparesheet"))
        self.comparesheet.clicked.connect(self.vscs_compare_sheet)
        
        
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 290, 411, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def vscs_compare_sheet(self):
        
        global new_vscs_address
        global old_vscs_address
        global out_put_address
        file_name=os.path.join(out_put_address,'VSCScompareResult.xls')
        csv_initialize()
        sheet_new_name = self.newsheetchoose.currentText()
        csv_write(0, 1, str(sheet_new_name),filename=file_name)
        sheet_old_name = self.oldsheetchoose.currentText()
        csv_write(1, 1, str(sheet_old_name),filename=file_name)
        data_new = xlrd.open_workbook(str(new_vscs_address))
        data_old = xlrd.open_workbook(str(old_vscs_address))
        sheet_new = data_new.sheet_by_name(str(sheet_new_name))
        sheet_old = data_old.sheet_by_name(str(sheet_old_name))
        nrows_new = sheet_new.nrows #行数
        nrows_old = sheet_old.nrows #行数
        self.progressBar.setRange(5,nrows_new)
        dict_new={}
        dict_old={}

        for row_old in range(5,nrows_old):
            configurename1 = sheet_old.cell(row_old,2).value.encode('utf-8')
            configurename1=str(configurename1).replace(' ','').replace(',','')
            #configurename2 = sheet_old.cell(row_old,6).value.encode('utf-8')
            configurename2 = sheet_old.cell(row_old,6).value
            configurename2=str(configurename2).replace(' ','').replace(',','')
            configurename=configurename1+'0B'+configurename2
            
            configurevalue = sheet_old.cell(row_old,8).value.encode('utf-8')
            dict_old[str(configurename)]=str(configurevalue)
            #self.progressBar.setValue(row_old+1)
               
        row_write = 3
        for row_new in range(5,nrows_new):
            configurename1 = sheet_new.cell(row_new,2).value.encode('utf-8')
            configurename1=str(configurename1).replace(' ','').replace(',','')
            #configurename2 = sheet_new.cell(row_new,6).value.encode('utf-8')
            configurename2 = sheet_new.cell(row_new,6).value
            configurename2=str(configurename2).replace(' ','').replace(',','')
            configurename=configurename1+'0B'+configurename2
            
            configurevalue = sheet_new.cell(row_new,8).value.encode('utf-8')
            dict_new[str(configurename)]=str(configurevalue)
            
            if dict_old.get(str(configurename))==None:
                csv_write(row_write, 0, str(configurename),filename=file_name)
                csv_write(row_write, 1, 'Not Found',filename=file_name)
                csv_write(row_write, 2, str(configurevalue),filename=file_name)
                row_write= row_write+1 
            else:
                if dict_new.get(str(configurename))==dict_old.get(str(configurename)):
                    pass
                else:
                    old_value = dict_old.get(str(configurename))
                    csv_write(row_write, 0, str(configurename),filename=file_name)
                    csv_write(row_write, 1, 'Not Equal',filename=file_name)
                    csv_write(row_write, 2, str(configurevalue),filename=file_name)
                    csv_write(row_write, 3, str(old_value),filename=file_name)
                    row_write=row_write+1                   
            
            self.progressBar.setValue(row_new+1)
            
        

    def compare_vscs_part2_partnumber(self):
        global new_vscs_address
        global old_vscs_address
        global out_put_address   
        
        file_name = os.path.join(out_put_address,'VSCSPartnumbercompareResult.xls')
        null_csv_initialize(file_name)
        
        data_new = xlrd.open_workbook(str(new_vscs_address))
        data_old = xlrd.open_workbook(str(old_vscs_address))
        
        sheet_new_name = data_new.sheet_names()
        sheet_old_name = data_old.sheet_names()
        sheet_new_name_dict = {}
        sheet_old_name_dict = {}
        '''
        sheet_new_name.remove('ByteBit decoder')
        sheet_new_name.remove('BB03-Issues')
        sheet_new_name.remove('ChangeLog')
        sheet_new_name.remove('Summary')
        sheet_new_name.remove('Macros')
        sheet_new_name.remove('Sheet1')
        
        sheet_old_name.remove('ByteBit decoder')
        sheet_old_name.remove('BB03-Issues')
        sheet_old_name.remove('ChangeLog')
        sheet_old_name.remove('Summary')
        sheet_old_name.remove('Macros')
        sheet_old_name.remove('Sheet1')
        '''
        
        '''
        csv_write(0, 0, 'NEW',sheetnum=0,filename=file_name)
        csv_write(0, 2, 'OLD',sheetnum=0,filename=file_name)
        csv_write(0, 4, 'RESULT',sheetnum=0,filename=file_name)
        '''
        
        self.progressBar.setRange(0,100)
        row=1
        for name in sheet_new_name:
            sheet_new = data_new.sheet_by_name(str(name))
            part_number = sheet_new.cell(2,1).value.encode('utf-8')           
            sheet_new_name_dict[name] = str(part_number)
            
            csv_write(row, 0, name,sheetnum=0,filename=file_name)
            csv_write(row, 1, part_number,sheetnum=0,filename=file_name)
            
            if name in sheet_old_name:
                sheet_old = data_old.sheet_by_name(str(name))
                part_number = sheet_old.cell(2,1).value.encode('utf-8')
                sheet_old_name_dict[name] = str(part_number)
                csv_write(row, 2, name,sheetnum=0,filename=file_name)
                csv_write(row, 3, part_number,sheetnum=0,filename=file_name)
                if sheet_old_name_dict[name] == sheet_new_name_dict[name]:
                    csv_write(row, 4, 'Same',sheetnum=0,filename=file_name)
                else:
                    csv_write(row, 4, 'Different',sheetnum=0,filename=file_name)
                sheet_old_name.remove(name)
            else:
                pass
            row = row+1

        if len(sheet_old_name)>0:
            for name in sheet_old_name:
                sheet_old = data_old.sheet_by_name(str(name)) 
                try:
                    part_number =  sheet_old.cell(2,1).value.encode('utf-8')
                    sheet_old_name_dict[name] = str(part_number)
                    csv_write(row, 2, name,sheetnum=0,filename=file_name)
                    csv_write(row, 3, part_number,sheetnum=0,filename=file_name)
                except:
                    continue
                row=row+1
        print(row)
        self.progressBar.setValue(100)   
        
        

        

    def vscs_copy(self):    #为了对比BCM
        '''
        QMessageBox.information(self.centralwidget,(_fromUtf8("好家伙！")),  
                                (_fromUtf8("你想累死我啊!")))  
        #self.label.setText("Information MessageBox")  
        '''
        global new_vscs_address
        global old_vscs_address
        global out_put_address
        
        sheet_new_name = self.newsheetchoose.currentText()
        sheet_old_name = self.oldsheetchoose.currentText()
        data_new = xlrd.open_workbook(str(new_vscs_address))
        data_old = xlrd.open_workbook(str(old_vscs_address))
        sheet_new = data_new.sheet_by_name(str(sheet_new_name))
        sheet_old = data_old.sheet_by_name(str(sheet_old_name))
        nrows_new = sheet_new.nrows #行数
        nrows_old = sheet_old.nrows #行数
        self.progressBar.setRange(5,nrows_new)
        dict_new={}
        dict_old={}
        
        
        
        
        for row_old in range(5,nrows_old):
            configurename1 = sheet_old.cell(row_old,2).value.encode('utf-8')
            configurename1=str(configurename1).replace(' ','').replace(',','')
            configurename2 = sheet_old.cell(row_old,6).value.encode('utf-8')
            configurename2=str(configurename2).replace(' ','').replace(',','')
            configurename=configurename1+'0B'+configurename2
            
            configurevalue = sheet_old.cell(row_old,8).value.encode('utf-8')
            dict_old[str(configurename)]=str(configurevalue)
            
            print(dict_old.get(str(configurename)))
            #self.progressBar.setValue(row_old+1)
               
        row_write = 3
        for row_new in range(5,nrows_new):
            configurename1 = sheet_new.cell(row_new,2).value.encode('utf-8')
            configurename1=str(configurename1).replace(' ','').replace(',','')
            configurename2 = sheet_new.cell(row_new,6).value.encode('utf-8')
            configurename2=str(configurename2).replace(' ','').replace(',','')
            configurename=configurename1+'0B'+configurename2
            print(configurename)
            if dict_old.get(str(configurename))==None:
                csv_write(row_new, 8, 'Not Found in old VSCS',sheetnum=6,filename=new_vscs_address)
            else:              
                csv_write(row_new, 8, dict_old.get(str(configurename)),sheetnum=6,filename=new_vscs_address)
                    
            
            self.progressBar.setValue(row_new+1)
            
        
        
        
        
        
        
    def choose_new_vscs(self):
        global new_vscs_address
        global old_vscs_address
        global out_put_address
        new_vscs_address = QtGui.QFileDialog.getOpenFileName(filter='*.xlsm;;*.xlsx;;*.xls;;All files(*)')
        self.newvscsaddress.append(str(new_vscs_address))
        data = xlrd.open_workbook(str(new_vscs_address))
        table = data.sheet_names()
        self.newsheetchoose.addItems(table)

        
        
        
        
        
    def choose_old_vscs(self):
        global new_vscs_address
        global old_vscs_address
        global out_put_address
        old_vscs_address = QtGui.QFileDialog.getOpenFileName(filter='*.xlsm;;*.xlsx;;*.xls;;All files(*)')
        self.oldvscsaddress.append(str(old_vscs_address))
        data = xlrd.open_workbook(str(old_vscs_address))
        table = data.sheet_names()
        self.oldsheetchoose.addItems(table)        
        

    def output_vscs(self):
        global new_vscs_address
        global old_vscs_address
        global out_put_address
        out_put_address = str(QtGui.QFileDialog.getExistingDirectory())
        self.outputaddressdisplay.append(str(out_put_address))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XcLVSCScompare", None))
        self.newvscs.setText(_translate("MainWindow", "New VSCS", None))
        self.newvscschoose.setText(_translate("MainWindow", "Browse", None))
        self.oldvscschoose.setText(_translate("MainWindow", "Browse", None))
        self.oldvscs.setText(_translate("MainWindow", "Old VSCS", None))
        self.copy.setText(_translate("MainWindow", "Copy", None))
        self.partnumber.setText(_translate("MainWindow", "Partnumber", None))
        self.outputaddress.setText(_translate("MainWindow", "Output Fold", None))
        self.outputaddresschoose.setText(_translate("MainWindow", "Browse", None))
        self.comparesheet.setText(_translate("MainWindow", "Compare Sheet", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        
 
def csv_write(row=0, col=0,content='NA',sheetnum=0,filename='C:\Users\jxue18\Desktop\VSCScompareResult.xls'):
    #参数分别为 行 列，内容，第几个sheet，文件名
    #global out_put_address #='VSCScompareResult.xls'
    #file_name=os.path.join(out_put_address,'VSCScompareResult.xls')
    old=xlrd.open_workbook(filename,formatting_info=True)
    new=copy(old)
    
    booksheet = new.get_sheet(sheetnum)
    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1
    style = xlwt.easyxf('align: wrap on,vert centre, horiz center') #自动换行、水平居中、垂直居中
    style.borders = borders
    booksheet.write(row,col,content,style)
    #booksheet.panes_frozen=True
    
    booksheet.horz_split_pos= 1
    
    new.save(filename)    

def csv_setting(): 
    global new_vscs_address
    global old_vscs_address
    global out_put_address
    filename = os.path.join(out_put_address,'VSCScompareResult.xls')
    if os.path.exists(filename):
        message = 'OK, the "%s" file exists.'
    else:
        csv_initialize()

def csv_initialize():
    global new_vscs_address
    global old_vscs_address
    global out_put_address
    workbook=xlwt.Workbook(encoding="utf-8")
    booksheet=workbook.add_sheet(u'sheet_1')
    booksheet.col(0).width= 20240
    booksheet.col(1).width= 5120
    booksheet.col(2).width= 5120
    booksheet.col(3).width= 5120
    row=1
    col=1
    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1
    style = xlwt.easyxf('align: wrap on,vert centre, horiz center') #自动换行、水平居中、垂直居中
    style.borders = borders
    title=xlwt.easyxf(u'font:name 仿宋,height 240 ,colour_index black, bold on, italic off; align: wrap on, vert centre, horiz center;pattern: pattern solid, fore_colour yellow;')
    title.borders = borders
    name='Configuration_name'
    result='Result'
    new_value='New_Value'
    old_value='Old_Value'
    booksheet.write(0,0,str(new_vscs_address),title)
    booksheet.write(1,0,str(old_vscs_address),title)
    booksheet.write(2,0,name,title)
    booksheet.write(2,1,result,title)
    booksheet.write(2,2,new_value,title)
    booksheet.write(2,3,old_value,title)
    #booksheet.panes_frozen=True
    booksheet.horz_split_pos= 1
    file_name = os.path.join(out_put_address,'VSCScompareResult.xls')
    workbook.save(file_name) 
 
def null_csv_initialize(file_name):
    global new_vscs_address
    global old_vscs_address
    global out_put_address
    workbook=xlwt.Workbook(encoding="utf-8")
    booksheet=workbook.add_sheet(u'sheet_1')
    booksheet.col(0).width= 5000
    booksheet.col(1).width= 10000
    booksheet.col(2).width= 5000
    booksheet.col(3).width= 10000
    booksheet.col(4).width= 5000
    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1
    title=xlwt.easyxf(u'font:name 仿宋,height 240 ,colour_index black, bold on, italic off; align: wrap on, vert centre, horiz center;pattern: pattern solid, fore_colour yellow;')
    title.borders = borders
    booksheet.write(0,0,'NEW',title)
    booksheet.write(0,1,'PARTNUMBER',title)
    booksheet.write(0,2,'OLD',title)
    booksheet.write(0,3,'PARTNUMBER',title)
    booksheet.write(0,4,'RESULT',title)
    
    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1
    booksheet.horz_split_pos= 1
    workbook.save(file_name) 
    
     
        
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    Compare = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Compare)
    Compare.show()
    sys.exit(app.exec_())