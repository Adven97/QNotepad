import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow):

    def getfiles(self):

            try:
                self.file_path = QFileDialog.getOpenFileName(self, 'Open File', './',
                                                             filter="Text Files(*.txt)")

                if self.file_path[0]:
                    self.file_name = (self.file_path[0].split('/'))[-1]

                    self.setWindowTitle("{} - QNotatnik".format(self.file_name))

                    file_open = open(self.file_path[0], 'r+')
                    self.statusBar().showMessage('Open... {}'.format(self.file_path[0]))

                    with file_open:
                        content = file_open.read()
                        self.form_widget.tree2.setPlainText(content)

            except UnicodeDecodeError as why:
                        self.error_box(why)
                        pass

    def saveInput(self):

        try:
            name = QFileDialog.getSaveFileName(self, "Save File", './', '.txt')[0]
            name = name+".txt"
            file = open(name, 'w')
        #    text = self.form_widget.tree2.text()
            lines = self.form_widget.tree2.document().toPlainText()
            with file:
                file.write(lines)
                file.close()

        except UnicodeDecodeError as why:
                    self.error_box(why)
                    pass


    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_widget = App()
        self.setCentralWidget(self.form_widget)

        self.setWindowTitle('QNotatnik')
        self.setGeometry(1, 1, 1600, 1200)
        self.setWindowIcon(QIcon('img/umowa.png'))
        self.setAutoFillBackground(True)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Plik')
        nowy = QAction('Nowy', self)
        otworz = QAction('Otwórz', self)
        otworz.triggered.connect(self.getfiles)
        zapisz = QAction('Zapisz', self)
        zapisz.triggered.connect(self.saveInput)
        zapiszjako = QAction('Zapisz jako...', self)
        zapiszjako.triggered.connect(self.saveInput)
        koniec = QAction('Koniec', self)
        koniec.triggered.connect(lambda: self.close())

        fileMenu.addAction(nowy)
        fileMenu.addAction(otworz)
        fileMenu.addAction(zapisz)
        fileMenu.addAction(zapiszjako)
        fileMenu.addAction(koniec)

        editMenu = mainMenu.addMenu('Edycja')
        wytnij = QAction('Wytnij', self)
        kopiuj = QAction('Kopiuj', self)
        wklej = QAction('Wklej', self)
        zaznacz = QAction('Zaznacz wszystko', self)

        editMenu.addAction(wytnij)
        editMenu.addAction(kopiuj)
        editMenu.addAction(wklej)
        editMenu.addAction(zaznacz)

        self.toolbar = self.addToolBar('')
        newAct = QAction(QIcon('img/1.png'), 'new', self)
        #newAct.setShortcut('Ctrl+Q')
        self.toolbar.addAction(newAct)
        open = QAction(QIcon("img/3.png"),"open",self)
        open.triggered.connect(self.getfiles)
        self.toolbar.addAction(open)
        search = QAction(QIcon("img/6.png"),"search",self)
        self.toolbar.addAction(search)
        save = QAction(QIcon("img/7.png"),"save",self)
        save.triggered.connect(self.saveInput)
        save.setShortcut('Ctrl+S')
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

    def btnstate(self,b):

      if b.text() == "Times New Roman":
         if b.isChecked() == True:
            self.font.setFamily("Times New Roman")
            #self.font.setPointSize(22)
            self.tree2.setFont(self.font)

      if b.text() == "Arial":
           if b.isChecked() == True:
              self.font.setFamily("Arial")
              #self.font.setPointSize(12)
              self.tree2.setFont(self.font)

      if b.text() == "Courier New":
           if b.isChecked() == True:
              self.font.setFamily("Courier New")
             # self.font.setPointSize(8)
              self.tree2.setFont(self.font)


    def on_click(self,color):
        def setcolor():
            self.tree2.setStyleSheet("background-color:"+color+";")
        return setcolor

    def selectionchange(self):
        self.font.setPointSize(int(self.combobox.currentText()))


    def initUI(self):

        vmain = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.font = QFont()

        self.tree = QVBoxLayout()
        self.combobox = QComboBox()
        self.combobox.addItem("8")
        self.combobox.addItem("9")
        self.combobox.addItem("10")
        self.combobox.addItem("11")
        self.combobox.addItem("12")
        self.combobox.addItem("14")
        self.combobox.addItem("16")
        self.combobox.addItem("18")
        self.combobox.addItem("20")
        self.combobox.addItem("22")
        self.combobox.addItem("24")
        self.combobox.currentIndexChanged.connect(self.selectionchange)

        self.rb1 = QRadioButton('Times New Roman')
        self.rb1.toggled.connect(lambda:self.btnstate(self.rb1))
        self.rb2 = QRadioButton('Arial')
        self.rb2.toggled.connect(lambda:self.btnstate(self.rb2))
        self.rb3 = QRadioButton('Courier New')
        self.rb3.toggled.connect(lambda:self.btnstate(self.rb3))

        colors =['#181818','#808080', '#680000', '#F00000', '#CC6600',
                    '#ffffff', '#D0D0D0', '#CC6633', '#FF99FF', '#FFFF00',
                    '#FFFF66', '#99FF00', '#3399CC', '#330099', '#990099',
                    '#FFFF99', '#99FF66', '#66FFFF', '#6699FF', '#996699' ]

        colorbox = QGridLayout()
        for color in colors:
            inxd =colors.index(color)
            clr = QPushButton()
            clr.clicked.connect(self.on_click(color))
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


        self.tree.addWidget(self.combobox)
        self.tree.addWidget(self.rb1)
        self.tree.addWidget(self.rb2)
        self.tree.addWidget(self.rb3)
        self.tree.addLayout(colorbox)
        #self.tree.setSizeConstraint(QLayout.SetFixedSize)
        self.tree.setAlignment(Qt.AlignTop)

        self.tree2 = QTextEdit()
        self.tree2.setAutoFillBackground(True)

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
