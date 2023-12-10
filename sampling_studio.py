# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sampling_studio.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1573, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 743))
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QPushButton {\n"
"  background-color: #FF7300;\n"
"  color: white;\n"
"  border: none;\n"
"\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  cursor: pointer;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #192639;\n"
"  color: #eee;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: #676767;\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_clear.setFont(font)
        self.btn_clear.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_clear.setStyleSheet("background-color: #FF7300;")
        self.btn_clear.setAutoDefault(True)
        self.btn_clear.setDefault(True)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.dial_noise = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.dial_noise.sizePolicy().hasHeightForWidth())
        self.dial_noise.setSizePolicy(sizePolicy)
        self.dial_noise.setSizeIncrement(QtCore.QSize(500, 500))
        self.dial_noise.setObjectName("dial_noise")
        self.gridLayout.addWidget(self.dial_noise, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.btn_import = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_import.setFont(font)
        self.btn_import.setStyleSheet("background-color: #FF7300;")
        self.btn_import.setObjectName("btn_import")
        self.gridLayout.addWidget(self.btn_import, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(20, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid;\n"
"    border-color: rgb(255, 161, 46);\n"
"  border-radius: 5px;\n"
"    color: #333333;\n"
"    padding: 10px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
" subcontrol-position: top center;\n"
"  background-color:  rgb(255, 161, 46);\n"
"    subcontrol-origin: margin;\n"
" color:rgb(255, 255, 255);\n"
"    font: 14pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 40px;\n"
"    padding-right: 40px;\n"
"\n"
"}\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.spin_phase = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_phase.setObjectName("spin_phase")
        self.gridLayout_4.addWidget(self.spin_phase, 2, 1, 1, 1)
        self.spin_amp = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_amp.setObjectName("spin_amp")
        self.gridLayout_4.addWidget(self.spin_amp, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.btn_add_comp = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_comp.sizePolicy().hasHeightForWidth())
        self.btn_add_comp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_add_comp.setFont(font)
        self.btn_add_comp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_add_comp.setStyleSheet("background-color: #FF7300;")
        self.btn_add_comp.setAutoDefault(True)
        self.btn_add_comp.setDefault(True)
        self.btn_add_comp.setObjectName("btn_add_comp")
        self.gridLayout_4.addWidget(self.btn_add_comp, 3, 1, 1, 1)
        self.spin_freq = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_freq.setObjectName("spin_freq")
        self.gridLayout_4.addWidget(self.spin_freq, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255, 255, 255);\n"
"border: 2px solid  rgb(255, 170, 0);\n"
"border-radius:8px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)
        self.comb_bx_examp = QtWidgets.QComboBox(self.groupBox)
        self.comb_bx_examp.setStyleSheet(" border: 1px solid #ccc;\n"
"border-radius:5px;\n"
"font-family: Arial, sans-serif;\n"
"color: black;\n"
"background-color:rgb(25, 117, 255);\n"
"")
        self.comb_bx_examp.setObjectName("comb_bx_examp")
        self.comb_bx_examp.addItem("")
        self.comb_bx_examp.addItem("")
        self.comb_bx_examp.addItem("")
        self.comb_bx_examp.addItem("")
        self.gridLayout_4.addWidget(self.comb_bx_examp, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 2px solid;\n"
"    border-color: rgb(255, 161, 46);\n"
"  border-radius: 5px;\n"
"    color: #333333;\n"
"    padding: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
" subcontrol-position: top center;\n"
"  background-color:  rgb(255, 161, 46);\n"
"    subcontrol-origin: margin;\n"
" color:rgb(255, 255, 255);\n"
"    font: 14pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 40px;\n"
"    padding-right: 40px;\n"
"\n"
"}\n"
"QLabel {\n"
"    color: white;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_comps = QtWidgets.QListWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_comps.sizePolicy().hasHeightForWidth())
        self.list_comps.setSizePolicy(sizePolicy)
        self.list_comps.setObjectName("list_comps")
        self.verticalLayout_2.addWidget(self.list_comps)
        self.btn_remove = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_remove.setFont(font)
        self.btn_remove.setStyleSheet("background-color: #FF7300;")
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout_2.addWidget(self.btn_remove)
        self.btn_mixed_plot = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_mixed_plot.setFont(font)
        self.btn_mixed_plot.setStyleSheet("background-color: #FF7300;")
        self.btn_mixed_plot.setObjectName("btn_mixed_plot")
        self.verticalLayout_2.addWidget(self.btn_mixed_plot)
        self.gridLayout_4.addWidget(self.groupBox_3, 5, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_samp_freq = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_samp_freq.setFont(font)
        self.lbl_samp_freq.setObjectName("lbl_samp_freq")
        self.horizontalLayout_2.addWidget(self.lbl_samp_freq)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setStyleSheet("QSlider {\n"
"    border: 1px solid #000;\n"
"    background: #EEE;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"QSlider::handle {\n"
"    background: rgb(255, 161, 46);\n"
"    border: 1px solid #000;\n"
"    width: 10px;\n"
"\n"
"   \n"
"}\n"
"QSlider::groove {\n"
"    background: #CCC;\'\n"
"\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.btn_switch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_switch.setFont(font)
        self.btn_switch.setStyleSheet("background-color: #FF7300;\n"
"")
        self.btn_switch.setObjectName("btn_switch")
        self.horizontalLayout_2.addWidget(self.btn_switch)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_5.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.graph_orignal = PlotWidget(self.centralwidget)
        self.graph_orignal.setStyleSheet("")
        self.graph_orignal.setObjectName("graph_orignal")
        self.verticalLayout.addWidget(self.graph_orignal)
        spacerItem4 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.graph_recons = PlotWidget(self.centralwidget)
        self.graph_recons.setStyleSheet("QPlotGraph {\n"
"  background-color: #3498db;\n"
"  color: white;\n"
"  border: none;\n"
"  padding: 10px 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  cursor: pointer;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPlotGraph:hover {\n"
"  background-color: #192639;\n"
"  color: #eee;\n"
"}\n"
"")
        self.graph_recons.setObjectName("graph_recons")
        self.verticalLayout.addWidget(self.graph_recons)
        spacerItem5 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.graph_error = PlotWidget(self.centralwidget)
        self.graph_error.setObjectName("graph_error")
        self.verticalLayout.addWidget(self.graph_error)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1573, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spin_freq, self.spin_amp)
        MainWindow.setTabOrder(self.spin_amp, self.spin_phase)
        MainWindow.setTabOrder(self.spin_phase, self.btn_add_comp)
        MainWindow.setTabOrder(self.btn_add_comp, self.comb_bx_examp)
        MainWindow.setTabOrder(self.comb_bx_examp, self.list_comps)
        MainWindow.setTabOrder(self.list_comps, self.btn_remove)
        MainWindow.setTabOrder(self.btn_remove, self.btn_mixed_plot)
        MainWindow.setTabOrder(self.btn_mixed_plot, self.btn_import)
        MainWindow.setTabOrder(self.btn_import, self.dial_noise)
        MainWindow.setTabOrder(self.dial_noise, self.btn_clear)
        MainWindow.setTabOrder(self.btn_clear, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.graph_orignal)
        MainWindow.setTabOrder(self.graph_orignal, self.graph_recons)
        MainWindow.setTabOrder(self.graph_recons, self.graph_error)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_clear.setText(_translate("MainWindow", "Clear graphs"))
        self.label_7.setText(_translate("MainWindow", "SNR level"))
        self.btn_import.setText(_translate("MainWindow", "Import"))
        self.groupBox.setTitle(_translate("MainWindow", "Add signal"))
        self.label_6.setText(_translate("MainWindow", "Adjust amplitude"))
        self.label_5.setText(_translate("MainWindow", "Adjust frequency"))
        self.btn_add_comp.setText(_translate("MainWindow", "Add"))
        self.label_9.setText(_translate("MainWindow", "Ready templates"))
        self.comb_bx_examp.setItemText(0, _translate("MainWindow", "choose example"))
        self.comb_bx_examp.setItemText(1, _translate("MainWindow", "example 1 : sin(2πx (15) ) +sin(2πx(30))"))
        self.comb_bx_examp.setItemText(2, _translate("MainWindow", "example 2 : sin(2πx (10)) + sin(2πx(20))"))
        self.comb_bx_examp.setItemText(3, _translate("MainWindow", "example 3 : sin(2πx (30) ) + sin(2πx(60))  "))
        self.label_8.setText(_translate("MainWindow", "Adjust phase"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mixed signals"))
        self.btn_remove.setText(_translate("MainWindow", "Remove"))
        self.btn_mixed_plot.setText(_translate("MainWindow", "Plot"))
        self.label_4.setText(_translate("MainWindow", "Sampling range"))
        self.lbl_samp_freq.setText(_translate("MainWindow", "1fmax"))
        self.btn_switch.setText(_translate("MainWindow", "Switch to hz"))
        self.label.setText(_translate("MainWindow", "Original signal"))
        self.label_2.setText(_translate("MainWindow", "Reconstructed signal"))
        self.label_3.setText(_translate("MainWindow", "Calculated Error "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
from pyqtgraph import PlotWidget
