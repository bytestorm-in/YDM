# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabbedUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(406, 590)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.txtFolderList = QtGui.QLineEdit(self.tab)
        self.txtFolderList.setObjectName(_fromUtf8("txtFolderList"))
        self.gridLayout_2.addWidget(self.txtFolderList, 1, 2, 1, 1)
        self.btnFolderList = QtGui.QPushButton(self.tab)
        self.btnFolderList.setObjectName(_fromUtf8("btnFolderList"))
        self.gridLayout_2.addWidget(self.btnFolderList, 1, 3, 1, 1)
        self.lblUrl = QtGui.QLabel(self.tab)
        self.lblUrl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUrl.setObjectName(_fromUtf8("lblUrl"))
        self.gridLayout_2.addWidget(self.lblUrl, 0, 0, 1, 2)
        self.lblProgress = QtGui.QLabel(self.tab)
        self.lblProgress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProgress.setObjectName(_fromUtf8("lblProgress"))
        self.gridLayout_2.addWidget(self.lblProgress, 2, 0, 1, 2)
        self.lblFolder = QtGui.QLabel(self.tab)
        self.lblFolder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblFolder.setObjectName(_fromUtf8("lblFolder"))
        self.gridLayout_2.addWidget(self.lblFolder, 1, 0, 1, 2)
        self.txtUrlList = QtGui.QLineEdit(self.tab)
        self.txtUrlList.setText(_fromUtf8(""))
        self.txtUrlList.setObjectName(_fromUtf8("txtUrlList"))
        self.gridLayout_2.addWidget(self.txtUrlList, 0, 2, 1, 2)
        self.progressBarList = QtGui.QProgressBar(self.tab)
        self.progressBarList.setProperty("value", 24)
        self.progressBarList.setObjectName(_fromUtf8("progressBarList"))
        self.gridLayout_2.addWidget(self.progressBarList, 2, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.btnParseListLink = QtGui.QPushButton(self.tab)
        self.btnParseListLink.setObjectName(_fromUtf8("btnParseListLink"))
        self.verticalLayout.addWidget(self.btnParseListLink)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 337, 341))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.verticalScrollBar = QtGui.QScrollBar(self.tab)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.gridLayout_3.addWidget(self.verticalScrollBar, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.btnDownloadList = QtGui.QPushButton(self.tab)
        self.btnDownloadList.setObjectName(_fromUtf8("btnDownloadList"))
        self.verticalLayout.addWidget(self.btnDownloadList)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lblFolder2 = QtGui.QLabel(self.tab_2)
        self.lblFolder2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblFolder2.setObjectName(_fromUtf8("lblFolder2"))
        self.gridLayout_8.addWidget(self.lblFolder2, 2, 0, 1, 2)
        self.lblVidUrl = QtGui.QLabel(self.tab_2)
        self.lblVidUrl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblVidUrl.setObjectName(_fromUtf8("lblVidUrl"))
        self.gridLayout_8.addWidget(self.lblVidUrl, 1, 0, 1, 2)
        self.btnFolderVid = QtGui.QPushButton(self.tab_2)
        self.btnFolderVid.setObjectName(_fromUtf8("btnFolderVid"))
        self.gridLayout_8.addWidget(self.btnFolderVid, 2, 3, 1, 1)
        self.progressBarVideo = QtGui.QProgressBar(self.tab_2)
        self.progressBarVideo.setProperty("value", 0)
        self.progressBarVideo.setObjectName(_fromUtf8("progressBarVideo"))
        self.gridLayout_8.addWidget(self.progressBarVideo, 3, 2, 1, 2)
        self.txtUrlVid = QtGui.QLineEdit(self.tab_2)
        self.txtUrlVid.setObjectName(_fromUtf8("txtUrlVid"))
        self.gridLayout_8.addWidget(self.txtUrlVid, 1, 2, 1, 2)
        self.txtFolderVid = QtGui.QLineEdit(self.tab_2)
        self.txtFolderVid.setObjectName(_fromUtf8("txtFolderVid"))
        self.gridLayout_8.addWidget(self.txtFolderVid, 2, 2, 1, 1)
        self.lblProgress2 = QtGui.QLabel(self.tab_2)
        self.lblProgress2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProgress2.setObjectName(_fromUtf8("lblProgress2"))
        self.gridLayout_8.addWidget(self.lblProgress2, 3, 0, 1, 2)
        self.gridLayout_11.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.btnParseVidLink = QtGui.QPushButton(self.tab_2)
        self.btnParseVidLink.setObjectName(_fromUtf8("btnParseVidLink"))
        self.gridLayout_11.addWidget(self.btnParseVidLink, 1, 0, 1, 1)
        self.btnDownloadVid = QtGui.QPushButton(self.tab_2)
        self.btnDownloadVid.setEnabled(False)
        self.btnDownloadVid.setObjectName(_fromUtf8("btnDownloadVid"))
        self.gridLayout_11.addWidget(self.btnDownloadVid, 4, 0, 1, 1)
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_11.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.comboQuality = QtGui.QComboBox(self.tab_2)
        self.comboQuality.setObjectName(_fromUtf8("comboQuality"))
        self.gridLayout_5.addWidget(self.comboQuality, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.txtVidFilename = QtGui.QLineEdit(self.tab_2)
        self.txtVidFilename.setEnabled(True)
        self.txtVidFilename.setReadOnly(True)
        self.txtVidFilename.setObjectName(_fromUtf8("txtVidFilename"))
        self.gridLayout_5.addWidget(self.txtVidFilename, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_5, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.label = QtGui.QLabel(self.tab_5)
        self.label.setGeometry(QtCore.QRect(50, 80, 281, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "YDM 2.0", None))
        self.btnFolderList.setText(_translate("MainWindow", "Change Folder", None))
        self.lblUrl.setText(_translate("MainWindow", "Playlist URL:", None))
        self.lblProgress.setText(_translate("MainWindow", "Progress:", None))
        self.lblFolder.setText(_translate("MainWindow", "Download To:", None))
        self.btnParseListLink.setText(_translate("MainWindow", "Get Download Links", None))
        self.btnDownloadList.setText(_translate("MainWindow", "Download Checked", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Playlist Downloader", None))
        self.lblFolder2.setText(_translate("MainWindow", "Download To:", None))
        self.lblVidUrl.setText(_translate("MainWindow", "Video URL:", None))
        self.btnFolderVid.setText(_translate("MainWindow", "Change Folder", None))
        self.txtUrlVid.setText(_translate("MainWindow", "https://www.youtube.com/watch?v=B9nwrsNM4tk", None))
        self.lblProgress2.setText(_translate("MainWindow", "Progress:", None))
        self.btnParseVidLink.setText(_translate("MainWindow", "Get Download Link", None))
        self.btnDownloadVid.setText(_translate("MainWindow", "Download", None))
        self.label_2.setText(_translate("MainWindow", "Filename:      ", None))
        self.label_3.setText(_translate("MainWindow", "Quality:", None))
        self.txtVidFilename.setText(_translate("MainWindow", "-------------PRESS GET DOWNLOAD LINK-----------------------", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Single Video Downloader", None))
        self.label.setText(_translate("MainWindow", "CREATED BY STUDIOBYTESTORM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "About", None))

