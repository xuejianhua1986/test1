from distutils.core import setup
import py2exe
import unrar
import os
import unrar
from unrar import rarfile
from PyQt4 import QtCore, QtGui
import sys
import xlwt
import os
import xlrd
import string
import sys

setup(windows=[{"script":"compare.py", "icon_resources": [(1, "cd391.ico")]} ],options={"py2exe":{"includes":["sip"]}})