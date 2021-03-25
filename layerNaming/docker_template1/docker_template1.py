from krita import DockWidget

# Importing the relevant dependencies:
from PyQt5.QtCore import pyqtSlot, Qt, QPointF
from PyQt5.QtGui import (QStandardItem, QStandardItemModel, QPainter, QPalette,
                         QPixmap, QImage, QBrush, QPen, QIcon)
from PyQt5.QtWidgets import QWidget, QTabWidget, QListView, QVBoxLayout, QDialog, QHBoxLayout, QPushButton, QGridLayout, QApplication

DOCKER_TITLE = "layerMeimei"
# MEIMEI means naming in Japanese

class layerMeimei(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        listView = QListView()
        tabWidget = QTabWidget()

        self.tab1 = QListView()
        self.tab1.setViewMode(QListView.IconMode)
        self.tab1.setMovement(QListView.Static)
        self.tab1.setResizeMode(QListView.Adjust)
        self.tab1.setUniformItemSizes(True)
        self.tab1.setSelectionMode(QListView.SingleSelection)

        self.tab2 = QListView()
        self.tab2.setViewMode(QListView.IconMode)
        self.tab2.setMovement(QListView.Static)
        self.tab2.setResizeMode(QListView.Adjust)
        self.tab2.setUniformItemSizes(True)
        self.tab2.setSelectionMode(QListView.SingleSelection)

        self.tab3 = QListView()
        self.tab3.setViewMode(QListView.IconMode)
        self.tab3.setMovement(QListView.Static)
        self.tab3.setResizeMode(QListView.Adjust)
        self.tab3.setUniformItemSizes(True)
        self.tab3.setSelectionMode(QListView.SingleSelection)

        self.tab4 = QListView()
        self.tab4.setViewMode(QListView.IconMode)
        self.tab4.setMovement(QListView.Static)
        self.tab4.setResizeMode(QListView.Adjust)
        self.tab4.setUniformItemSizes(True)
        self.tab4.setSelectionMode(QListView.SingleSelection)

        self.tab5 = QListView()
        self.tab5.setViewMode(QListView.IconMode)
        self.tab5.setMovement(QListView.Static)
        self.tab5.setResizeMode(QListView.Adjust)
        self.tab5.setUniformItemSizes(True)
        self.tab5.setSelectionMode(QListView.SingleSelection)


        # Enter the name of the tab as you like
        tabWidget.addTab(self.tab1, i18n("1"))
        tabWidget.addTab(self.tab2, i18n("2"))
        tabWidget.addTab(self.tab3, i18n("3"))
        tabWidget.addTab(self.tab4, i18n("4"))
        tabWidget.addTab(self.tab5, i18n("5"))
        layout.addWidget(tabWidget)
        self.setWidget(widget)

        self.initUI1()
        self.initUI2()
        self.initUI3()
        self.initUI4()
        self.initUI5()

    def initUI1(self):
        grid = QGridLayout()
        self.setLayout(grid)

        #Enter the name of the layer as you like
        #Docker buttons line up in the same way as here
        names = ['Line', 'Color', 'Light', 'Shadow',
                 'A', 'B', 'C', 'D',
                '', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                '', '', '', ' ']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            koyuu = name
            button = QPushButton(koyuu, self)
            button.clicked.connect(self.layermeimei)
            grid.addWidget(button, *position)

        self.tab1.setLayout(grid)

    def initUI2(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Body', 'Hair', 'clothes', 'Shoes',
                 '', '', '', '',
                '', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                '', '', '', '']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            koyuu = name
            button = QPushButton(koyuu, self)
            button.clicked.connect(self.layermeimei)
            grid.addWidget(button, *position)

        self.tab2.setLayout(grid)

    def initUI3(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Ground', 'Sky', 'Building', '',
                 '', '', '', '',
                '', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                '', '', '', '']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            koyuu = name
            button = QPushButton(koyuu, self)
            button.clicked.connect(self.layermeimei)
            grid.addWidget(button, *position)

        self.tab3.setLayout(grid)


    def initUI4(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                '', '', '', '']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            koyuu = name
            button = QPushButton(koyuu, self)
            button.clicked.connect(self.layermeimei)
            grid.addWidget(button, *position)

        self.tab4.setLayout(grid)

    def initUI5(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                 '', '', '', '',
                '', '', '', '',
                '', '', '', '']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            koyuu = name
            button = QPushButton(koyuu, self)
            button.clicked.connect(self.layermeimei)
            grid.addWidget(button, *position)

        self.tab5.setLayout(grid)

    def layermeimei(self):
        sender = self.sender()
        application = Krita.instance()
        currentDoc = application.activeDocument()
        currentLayer = currentDoc.activeNode()
        currentLayer.setName(sender.text())

    def canvasChanged(self, canvas):
        pass
