import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_widget = App()
        self.setCentralWidget(self.form_widget)

        self.setWindowTitle('QNotatnik')
        self.setGeometry(1, 1, 1600, 1200)
        self.setWindowIcon(QIcon('img/umowa.png'))

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Plik')
        editMenu = mainMenu.addMenu('Edycja')

        self.toolbar = self.addToolBar('Exit')

        newAct = QAction(QIcon('img/1.png'), 'new', self)
        #newAct.setShortcut('Ctrl+Q')
        self.toolbar.addAction(newAct)
        open = QAction(QIcon("img/3.png"),"open",self)
        self.toolbar.addAction(open)
        search = QAction(QIcon("img/6.png"),"search",self)
        self.toolbar.addAction(search)
        save = QAction(QIcon("img/7.png"),"save",self)
        self.toolbar.addAction(save)

        undo = QAction(QIcon("img/2.png"),"undo",self)
        self.toolbar.addAction(undo)
        redo = QAction(QIcon("img/5.png"),"redo",self)
        self.toolbar.addAction(redo)

        cut = QAction(QIcon("img/4.png"),"cut",self)
        cut.setShortcut('Ctrl+X')
        self.toolbar.addAction(cut)
        copy = QAction(QIcon("img/9.png"),"copy",self)
        copy.setShortcut('Ctrl+C')
        self.toolbar.addAction(copy)
        paste = QAction(QIcon("img/8.png"),"paste",self)
        paste.setShortcut('Ctrl+V')
        self.toolbar.addAction(paste)

        self.statusBar().showMessage('Status bar (opisuje ostatnio wykonaną czynność)')


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vmain = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath('')


        self.tree = QVBoxLayout()
        combobox = QComboBox()
        combobox.addItem("8")
        combobox.addItem("9")
        combobox.addItem("10")
        combobox.addItem("11")
        combobox.addItem("12")
        combobox.addItem("14")
        combobox.addItem("16")
        combobox.addItem("18")
        combobox.addItem("20")
        combobox.addItem("22")
        combobox.addItem("24")
        rb1 = QRadioButton('Times New Roman')
        rb2 = QRadioButton('Arial')
        rb3 = QRadioButton('Courier New')

        colors =['#000000','#808080', '#680000', '#F00000', '#CC6600',
                    '#ffffff', '#D0D0D0', '#CC6633', '#FF99FF', '#FFFF00',
                    '#FFFF66', '#99FF00', '#3399CC', '#330099', '#990099',
                    '#FFFF99', '#99FF66', '#66FFFF', '#6699FF', '#996699' ]

        colorbox = QGridLayout()
        for color in colors:
            inxd =colors.index(color)
            clr = QPushButton()
            clr.setFixedWidth(35)
            clr.setFixedHeight(35)
            clr.setStyleSheet("background-color:"+color+";");
            if(inxd >=0 and inxd <5):
                colorbox.addWidget(clr,0,inxd)
            elif(inxd >=5 and inxd <10):
                colorbox.addWidget(clr,1,inxd -5)
            elif(inxd >=10 and inxd <15):
                colorbox.addWidget(clr,2,inxd -10)
            elif(inxd >=15 and inxd <20):
                colorbox.addWidget(clr,3,inxd -15)


        self.tree.addWidget(combobox)
        self.tree.addWidget(rb1)
        self.tree.addWidget(rb2)
        self.tree.addWidget(rb3)
        self.tree.addLayout(colorbox)
        #self.tree.setSizeConstraint(QLayout.SetFixedSize)
        self.tree.setAlignment(Qt.AlignTop)

        self.tree2 = QTextEdit()
    #    self.tree2.setFixedWidth(1050)

        ###     b1.setIcon(QIcon('tc.png'))     ustawienie img na przycisk

        windowLayout = QHBoxLayout()
        windowLayout.addLayout(self.tree)
        windowLayout.addWidget(self.tree2)
        vmain.addLayout(windowLayout)


        self.setLayout(vmain)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
