import sys

from PyQt5.QtCore import QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMdiSubWindow, QTextBrowser, QPlainTextEdit
from modfab_ui import Ui_mainWindow
from CLaunch import CLaunch
from CElModule import CElModule
from CSpecification import CSpecification


class Window(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.verticalLayoutWidget)
        self.connect_signals()

    def connect_signals(self):
        self.action.triggered.connect(self.open_file_selection)


    def open_file_selection(self):
        dialog = QFileDialog()
        file = dialog.getOpenFileName()
        launch_file_name = file[0]
        print('ok')
        subwindow = QMdiSubWindow()
        text = QPlainTextEdit()
        text.setReadOnly(True)
        subwindow.setWindowTitle(launch_file_name.split('/')[-1])
        subwindow.setWidget(text)
        self.mdiArea.addSubWindow(subwindow)
        print('ok')
        subwindow.showMaximized()
        cz = CLaunch(launch_file_name)
        text.insertPlainText(cz.rpt())
        print('ok')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


