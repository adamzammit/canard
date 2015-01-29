# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/responseTime.ui'
#
# Created: Sun Nov 30 11:27:10 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(505, 356)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.displayHint = QtGui.QLineEdit(Form)
        self.displayHint.setEnabled(False)
        self.displayHint.setText(_fromUtf8(""))
        self.displayHint.setObjectName(_fromUtf8("displayHint"))
        self.gridLayout.addWidget(self.displayHint, 1, 1, 1, 3)
        self.removeLanguage = QtGui.QPushButton(Form)
        self.removeLanguage.setMaximumSize(QtCore.QSize(30, 16777215))
        self.removeLanguage.setObjectName(_fromUtf8("removeLanguage"))
        self.gridLayout.addWidget(self.removeLanguage, 0, 3, 1, 1)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 5, 1, 1, 3)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.hasMinValue = QtGui.QCheckBox(Form)
        self.hasMinValue.setObjectName(_fromUtf8("hasMinValue"))
        self.gridLayout.addWidget(self.hasMinValue, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.maxValueHint = QtGui.QLineEdit(Form)
        self.maxValueHint.setEnabled(False)
        self.maxValueHint.setObjectName(_fromUtf8("maxValueHint"))
        self.gridLayout.addWidget(self.maxValueHint, 7, 1, 1, 3)
        self.minValueHint = QtGui.QLineEdit(Form)
        self.minValueHint.setEnabled(False)
        self.minValueHint.setObjectName(_fromUtf8("minValueHint"))
        self.gridLayout.addWidget(self.minValueHint, 4, 1, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 8, 1, 1, 3)
        self.minValue = QtGui.QTimeEdit(Form)
        self.minValue.setEnabled(False)
        self.minValue.setCalendarPopup(False)
        self.minValue.setObjectName(_fromUtf8("minValue"))
        self.gridLayout.addWidget(self.minValue, 3, 1, 1, 3)
        self.hasMaxValue = QtGui.QCheckBox(Form)
        self.hasMaxValue.setObjectName(_fromUtf8("hasMaxValue"))
        self.gridLayout.addWidget(self.hasMaxValue, 6, 0, 1, 1)
        self.maxValue = QtGui.QTimeEdit(Form)
        self.maxValue.setEnabled(False)
        self.maxValue.setCalendarPopup(False)
        self.maxValue.setObjectName(_fromUtf8("maxValue"))
        self.gridLayout.addWidget(self.maxValue, 6, 1, 1, 3)
        self.hasDisplayHint = QtGui.QCheckBox(Form)
        self.hasDisplayHint.setObjectName(_fromUtf8("hasDisplayHint"))
        self.gridLayout.addWidget(self.hasDisplayHint, 1, 0, 1, 1)
        self.addLanguage = QtGui.QPushButton(Form)
        self.addLanguage.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addLanguage.setObjectName(_fromUtf8("addLanguage"))
        self.gridLayout.addWidget(self.addLanguage, 0, 2, 1, 1)
        self.languages = QtGui.QComboBox(Form)
        self.languages.setEditable(False)
        self.languages.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.languages.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.languages.setObjectName(_fromUtf8("languages"))
        self.gridLayout.addWidget(self.languages, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.hasMinValue, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.minValueHint.setEnabled)
        QtCore.QObject.connect(self.hasMaxValue, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.maxValueHint.setEnabled)
        QtCore.QObject.connect(self.hasDisplayHint, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.displayHint.setEnabled)
        QtCore.QObject.connect(self.hasMinValue, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.minValue.setEnabled)
        QtCore.QObject.connect(self.hasMaxValue, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.maxValue.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.languages, self.displayHint)
        Form.setTabOrder(self.displayHint, self.minValue)
        Form.setTabOrder(self.minValue, self.minValueHint)
        Form.setTabOrder(self.minValueHint, self.maxValue)
        Form.setTabOrder(self.maxValue, self.maxValueHint)
        Form.setTabOrder(self.maxValueHint, self.hasMinValue)
        Form.setTabOrder(self.hasMinValue, self.hasMaxValue)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.displayHint.setPlaceholderText(QtGui.QApplication.translate("Form", "Optionally shown to assist with the response (like a placeholder like this)", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLanguage.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Hint", None, QtGui.QApplication.UnicodeUTF8))
        self.hasMinValue.setText(QtGui.QApplication.translate("Form", "Minimum Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Hint", None, QtGui.QApplication.UnicodeUTF8))
        self.hasMaxValue.setText(QtGui.QApplication.translate("Form", "Maximum Time", None, QtGui.QApplication.UnicodeUTF8))
        self.hasDisplayHint.setText(QtGui.QApplication.translate("Form", "Display Hint", None, QtGui.QApplication.UnicodeUTF8))
        self.addLanguage.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
