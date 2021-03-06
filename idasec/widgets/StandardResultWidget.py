from PySide import QtGui, QtCore
from PySide.QtGui import QWidget

class StandardResultWidget(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.action_selector.setEnabled(False)
        self.action_button.setEnabled(False)
        for k in self.parent.actions.keys():

            self.action_selector.addItem(k)
        self.action_button.clicked.connect(self.action_clicked)
        self.connect(self.action_selector, QtCore.SIGNAL("currentIndexChanged(QString)"), self.action_selector_changed)

    def action_selector_changed(self, s):
        _, enabled = self.parent.actions[s]
        if enabled:
            self.action_button.setText("Undo !")
        else:
            self.action_button.setText("Do !")

    def action_clicked(self):
        s = self.action_selector.currentText()
        fun, enabled = self.parent.actions[s]
        fun(enabled)

    def set_actions_visible_and_enabled(self, enable):
        self.action_label.setVisible(enable)
        self.action_selector.setVisible(enable)
        self.action_button.setVisible(enable)
        self.action_selector.setEnabled(enable)
        self.action_button.setEnabled(enable)

    def setupUi(self, standard_result):
        def _fromUtf8(s):
            return s
        def _translate(x,y,z):
            return y
        standard_result.setObjectName(_fromUtf8("standard_result"))
        standard_result.resize(495, 416)
        self.verticalLayout = QtGui.QVBoxLayout(standard_result)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webview = QtGui.QTextBrowser(standard_result)
        self.webview.setObjectName(_fromUtf8("webview"))
        self.verticalLayout.addWidget(self.webview)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.action_label = QtGui.QLabel(standard_result)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_label.sizePolicy().hasHeightForWidth())
        self.action_label.setSizePolicy(sizePolicy)
        self.action_label.setObjectName(_fromUtf8("action_label"))
        self.horizontalLayout_2.addWidget(self.action_label)
        self.action_selector = QtGui.QComboBox(standard_result)
        self.action_selector.setObjectName(_fromUtf8("action_selector"))
        self.horizontalLayout_2.addWidget(self.action_selector)
        self.action_button = QtGui.QPushButton(standard_result)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_button.sizePolicy().hasHeightForWidth())
        self.action_button.setSizePolicy(sizePolicy)
        self.action_button.setMinimumSize(QtCore.QSize(70, 0))
        self.action_button.setObjectName(_fromUtf8("action_button"))
        self.horizontalLayout_2.addWidget(self.action_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        QtCore.QMetaObject.connectSlotsByName(standard_result)
        standard_result.setWindowTitle(_translate("standard_result", "Form", None))
        self.action_label.setText(_translate("standard_result", "Action:", None))
        self.action_button.setText(_translate("standard_result", "Do !", None))