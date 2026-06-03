from PySide6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self._createCentralWidget()

    def _createCentralWidget(self):

        self._dataWidget = QtWidgets.QWidget()
        self._plotWidget = QtWidgets.QWidget()

        tabWidget = QtWidgets.QTabWidget()

        tabWidget.addTab(self._dataWidget, "Données")
        tabWidget.addTab(self._plotWidget, "Graphes")

        self.setCentralWidget(tabWidget)