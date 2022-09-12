import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

class SadWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Add title
        self.setWindowTitle("JP is SAD !!!")
        # Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        # Create a Label
        my_label = qtw.QLabel("Talk to JP.... only solution")
        # Change the font size of Label
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)  

        # Show SadWindow
        self.show()
