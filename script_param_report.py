#!/usr/bin/env python2
# coding: utf8
from pywinauto import Application,mouse , keyboard
from time import sleep
from subprocess import call
from os import environ, path, devnull, getcwd
from win32api import GetSystemMetrics

from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import os
import linecache

def genIni():
    iniFileObject = open(r"C:\\Jenkins\\CrystalDiskMark8\\DiskMark64.ini","w")
    iniFileObject.write("[Setting]\n")
    iniFileObject.write("TestData=0\n")
    iniFileObject.write("Language=English\n")
    iniFileObject.write("Theme=default\n")
    iniFileObject.write("TestUnit=0\n")
    iniFileObject.write("TestCount=4\n")
    iniFileObject.write("TestSize=6\n")
    iniFileObject.write("DriveLetter=3\n")
    iniFileObject.write("Settings=1\n")
    iniFileObject.write("Profile=0\n")
    iniFileObject.write("Benchmark=3\n")
    iniFileObject.write("BenchType0=0\n")
    iniFileObject.write("BenchSize0=128\n")
    iniFileObject.write("BenchQueues0=Queues\n")
    iniFileObject.write("BenchThreads0=core\n")
    iniFileObject.write("BenchType1=1\n")
    iniFileObject.write("BenchSize1=4\n")
    iniFileObject.write("BenchQueues1=Queues\n")
    iniFileObject.write("BenchThreads1=core\n")
    iniFileObject.write("BenchType2=0\n")
    iniFileObject.write("BenchSize2=128\n")
    iniFileObject.write("BenchQueues2=1\n")
    iniFileObject.write("BenchThreads2=1\n")
    iniFileObject.write("BenchType3=1\n")
    iniFileObject.write("BenchSize3=4\n")
    iniFileObject.write("BenchQueues3=1\n")
    iniFileObject.write("BenchThreads3=1\n")
    iniFileObject.write("BenchType4=0\n")
    iniFileObject.write("BenchSize4=128\n")
    iniFileObject.write("BenchQueues4=32\n")
    iniFileObject.write("BenchThreads4=4\n")
    iniFileObject.write("BenchType5=1\n")
    iniFileObject.write("BenchSize5=4\n")
    iniFileObject.write("BenchQueues5=32\n")
    iniFileObject.write("BenchThreads5=4\n")
    iniFileObject.write("BenchType6=0\n")  
    iniFileObject.write("BenchSize6=128\n")
    iniFileObject.write("BenchQueues6=32\n")  
    iniFileObject.write("BenchThreads6=4\n")
    iniFileObject.write("Affinity=1\n")  
    iniFileObject.write("MeasureTime=5\n")
    iniFileObject.write("IntervalTime=5\n")  

    iniFileObject.close()

mainWindowTitle = r"CrystalDiskMark 8.0.1 x64 [Admin]"
programToExcute = r"C:\\Jenkins\\CrystalDiskMark8\\DiskMark64.exe"
testDrivePosition = 1
Queues = linecache.getline(r"C:\\Jenkins-Report\\www.txt", 1)
core = linecache.getline(r"C:\\Jenkins-Report\\www.txt", 2)
resaultFile = path.join("C:\\Jenkins\\CrystalDiskMark8",'CrystalDiskMark-result.txt')
imageFile = path.join("C:\\Jenkins\\CrystalDiskMark8",'CrystalDiskMark-status.png')
genIni()
mouse.click(coords=(GetSystemMetrics(0),GetSystemMetrics(1)))
mainWindowTitleSimple = mainWindowTitle
app = Application(backend="uia").start(programToExcute)
sleep(1)

appWin32 = Application().connect(title=mainWindowTitle)
appWin32.CrystalDiskMark.MoveWindow(0, 0)
markApp = app.CrystalDiskMark
testAllBtn = markApp.child_window(title="All", control_type="Button")
testAllBtn.click_input()

stopMenu = markApp.child_window(title="Stop", auto_id="All", control_type="Button")
sleep(10)
markApp.wait('enabled', timeout=99999999999)
SetForegroundWindow(find_window(title=mainWindowTitle))

TEST_PASS = True
TEST_MESSAGE = ""
REPORT_MESSAGE = ""
markApp.menu_select("File->Save<text>")
appSaveDialog = markApp.child_window(title="Save As", control_type="Window")
appSaveDialogFName = appSaveDialog.child_window(title="File name:", auto_id="SaveDialogLabel", control_type="Text")
appSaveDialogFName.type_keys(resaultFile)
sleep(3)
appSaveDialog.child_window(title="Save", auto_id="1", control_type="Button").click()
sleep(3)
markApp.menu_select("File->Save <image>")
appSaveDialog = markApp.child_window(title="Save As", control_type="Window")
appSaveDialogFName = appSaveDialog.child_window(title="File name:", auto_id="SaveDialogLabel", control_type="Text")
appSaveDialogFName.type_keys(imageFile)
sleep(3)
appSaveDialog.child_window(title="Save", auto_id="1", control_type="Button").click()

exit(0)
