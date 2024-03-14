# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
import scheduleOperations, os, time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 517)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.overallFrame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overallFrame.sizePolicy().hasHeightForWidth())
        self.overallFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.overallFrame.setFont(font)
        self.overallFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.overallFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.overallFrame.setObjectName("overallFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.overallFrame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QFrame(parent=self.overallFrame)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.headerLabel.setMaximumSize(QtCore.QSize(16777215, 167))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("")
        self.headerLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.label = QtWidgets.QLabel(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.addSchedBtn = QtWidgets.QPushButton(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSchedBtn.sizePolicy().hasHeightForWidth())
        self.addSchedBtn.setSizePolicy(sizePolicy)
        self.addSchedBtn.setMinimumSize(QtCore.QSize(337, 27))
        self.addSchedBtn.setObjectName("addSchedBtn")
        self.gridLayout.addWidget(self.addSchedBtn, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.formLayout.setContentsMargins(50, 0, 50, -1)
        self.formLayout.setObjectName("formLayout")
        self.dayLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.dayLabel.setObjectName("dayLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dayLabel)
        self.dayDropdown = QtWidgets.QComboBox(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayDropdown.sizePolicy().hasHeightForWidth())
        self.dayDropdown.setSizePolicy(sizePolicy)
        self.dayDropdown.setMinimumSize(QtCore.QSize(135, 21))
        self.dayDropdown.setObjectName("dayDropdown")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.dayDropdown.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dayDropdown)
        self.subjectNameLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.subjectNameLabel.setObjectName("subjectNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.subjectNameLabel)
        self.subjectNameInput = QtWidgets.QLineEdit(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subjectNameInput.sizePolicy().hasHeightForWidth())
        self.subjectNameInput.setSizePolicy(sizePolicy)
        self.subjectNameInput.setMinimumSize(QtCore.QSize(135, 21))
        self.subjectNameInput.setMaximumSize(QtCore.QSize(135, 21))
        self.subjectNameInput.setObjectName("subjectNameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.subjectNameInput)
        self.startTimeLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.startTimeLabel)
        self.startTimeInput = QtWidgets.QTimeEdit(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTimeInput.sizePolicy().hasHeightForWidth())
        self.startTimeInput.setSizePolicy(sizePolicy)
        self.startTimeInput.setMinimumSize(QtCore.QSize(135, 22))
        self.startTimeInput.setObjectName("startTimeInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.startTimeInput)
        self.endTimeLabel = QtWidgets.QLabel(parent=self.headerFrame)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.endTimeLabel)
        self.endTimeInput = QtWidgets.QTimeEdit(parent=self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endTimeInput.sizePolicy().hasHeightForWidth())
        self.endTimeInput.setSizePolicy(sizePolicy)
        self.endTimeInput.setMinimumSize(QtCore.QSize(135, 22))
        self.endTimeInput.setObjectName("endTimeInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.endTimeInput)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.headerFrame)
        self.footerFrame = QtWidgets.QFrame(parent=self.overallFrame)
        self.footerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.footerFrame.setObjectName("footerFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footerFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label2 = QtWidgets.QLabel(parent=self.footerFrame)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label2.setObjectName("label2")
        self.verticalLayout_3.addWidget(self.label2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filenameLabel = QtWidgets.QLabel(parent=self.footerFrame)
        self.filenameLabel.setObjectName("filenameLabel")
        self.horizontalLayout_3.addWidget(self.filenameLabel)
        self.filenameInput = QtWidgets.QLineEdit(parent=self.footerFrame)
        self.filenameInput.setObjectName("filenameInput")
        self.horizontalLayout_3.addWidget(self.filenameInput)
        self.docxLabel = QtWidgets.QLabel(parent=self.footerFrame)
        self.docxLabel.setObjectName("docxLabel")
        self.horizontalLayout_3.addWidget(self.docxLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.generateSchedBtn = QtWidgets.QPushButton(parent=self.footerFrame)
        self.generateSchedBtn.setObjectName("generateSchedBtn")
        self.verticalLayout_3.addWidget(self.generateSchedBtn)
        self.verticalLayout.addWidget(self.footerFrame)
        self.horizontalLayout_2.addWidget(self.overallFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 397, 22))
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_File = QtGui.QAction(parent=MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.menuFile.addAction(self.actionLoad_File)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.actionLoad_File.triggered.connect(self.loadFile)
        self.addSchedBtn.clicked.connect(self.addSchedule)
        self.generateSchedBtn.clicked.connect(self.generateSchedule)

        # default loaded file name
        self.loadedFileName = "template.docx"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Class Schedule Generator"))
        MainWindow.setWindowIcon(QIcon("assets/images/scheduleIcon.png"))
        self.headerLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Class Schedule Generator</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Cambria\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Specify the day, name of subject, start and end </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">time, then click &quot;Add Schedule&quot;. Repeat until your </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">schedule is complete.</span></p></body></html>"))
        self.addSchedBtn.setText(_translate("MainWindow", "Add Schedule"))
        self.dayLabel.setText(_translate("MainWindow", "Day"))
        self.dayDropdown.setItemText(0, _translate("MainWindow", "Monday"))
        self.dayDropdown.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.dayDropdown.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.dayDropdown.setItemText(3, _translate("MainWindow", "Thursday"))
        self.dayDropdown.setItemText(4, _translate("MainWindow", "Friday"))
        self.dayDropdown.setItemText(5, _translate("MainWindow", "Saturday"))
        self.dayDropdown.setItemText(6, _translate("MainWindow", "Sunday"))
        self.subjectNameLabel.setText(_translate("MainWindow", "Subject Name"))
        self.startTimeLabel.setText(_translate("MainWindow", "Start Time"))
        self.endTimeLabel.setText(_translate("MainWindow", "End Time"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Once you\'re finished, specify the name of the output </span></p><p align=\"center\"><span style=\" font-size:11pt;\">file and click &quot;Generate Schedule&quot;.</span></p></body></html>"))
        self.filenameLabel.setText(_translate("MainWindow", "Filename"))
        self.docxLabel.setText(_translate("MainWindow", ".docx"))
        self.generateSchedBtn.setText(_translate("MainWindow", "Generate Schedule"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File"))
        self.actionLoad_File.setStatusTip(_translate("MainWindow", "Load an existing schedule to be modified."))

    def loadFile(self):
        # load an existing schedule
        openedFile = QFileDialog.getOpenFileName(parent=self.menuBar, 
                                               directory=os.path.expanduser('~'), 
                                               caption="Select a file.", 
                                               filter="Word Documents (*.docx)")
        # only show the filename instead of the full directory
        self.loadedFileName = openedFile[0].split(sep="/")[-1]

        if self.loadedFileName.strip() != "":
            self.loadedFilePopup(self.loadedFileName) 

    def addSchedule(self):
        day = self.dayDropdown.currentText()
        subject_name = self.subjectNameInput.text()
        start_time = time.strptime(self.startTimeInput.text(), "%I:%M %p") # convert to struct_time for sorting purposes
        end_time = self.endTimeInput.text()
        
        scheduleOperations.ADD_SCHEDS.append([day, subject_name, start_time, end_time])
        self.addSchedPopup()

    def generateSchedule(self):
        self.saveFileName = self.filenameInput.text()

        if self.saveFileName.lower() == "template":
            self.generateSchedulePopup(3) 
            return
        
        generateSchedFailed = scheduleOperations.generate_sched(loadFileName=self.loadedFileName, saveFileName=self.saveFileName)

        if generateSchedFailed:
            # depending on the error code returned by generateSchedFailed, show the appropriate error defined in generateSchedulePopup
            self.generateSchedulePopup(generateSchedFailed) 
            return
        
        # pop up schedule generated succesfully.
        self.generateSchedulePopup(0) # 0 means nothing went wrong
    
    def addSchedPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Successful")
        msg.setText("Schedule added successfully.")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def generateSchedulePopup(self, code: int):
        msg = QMessageBox()
        
        match code:
            case 1:
                msg.setWindowTitle("Unsuccessful")
                msg.setText("Failed to generate schedule. Make sure to give proper inputs.")
                msg.setIcon(QMessageBox.Icon.Warning)
            case 2:
                msg.setWindowTitle("Unsuccessful")
                msg.setText(f"{self.saveFileName}.docx is currently open. Please close the file and try again.")
                msg.setIcon(QMessageBox.Icon.Warning)
            case 3:
                msg.setWindowTitle("Unsuccessful")
                msg.setText("Please name the output file anything but template.docx.")
                msg.setIcon(QMessageBox.Icon.Warning)
            case _:
                msg.setWindowTitle("Successful")
                msg.setText("Schedule generated successfully. Please check the Schedules folder.")
                msg.setIcon(QMessageBox.Icon.Information)
            
        msg.exec()
    
    def loadedFilePopup(self, filename):
        msg = QMessageBox()
        msg.setWindowTitle("Successful")
        msg.setText(f"Successfully loaded {filename}.")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())