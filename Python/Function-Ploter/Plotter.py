# Pyside2 GUI libraries
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QDoubleSpinBox, QMessageBox, QStatusBar
from PySide2.QtGui import QPixmap, QPalette, QColor
from PySide2.QtCore import QSize, Qt
# Plotter libraries
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
# Processing libraries
import numpy as np
import sys
import re

# Constants
allowed_inputs = ("x", "/", "*", "-", "+", "^", "sin", "cos", "tan", "e")
replaced_inputs = {
    "sin": "np.sin",
    "cos": "np.cos",
    "e": "np.exp",
    "^": "**"
    }

# Convert input function to a mathematical expression
def in2func(inp):
    """Function converts input expression to a mathematical expression."""
    # Validate Function
    if inp == "":
        raise ValueError( f"Enter a function to plot!")
    for char in re.findall("[a-zA-Z_]+", inp):
        if char not in allowed_inputs:
            # Error will communicate over stderr pipeline
            raise ValueError( f"'{char}' is not in the allowed as an input character!")
            return
    # Replace allowed chars with suitable methods for eval compiling.
    for before, after in replaced_inputs.items():
        inp = inp.replace(before, after)
    # Edge Case: When no 'x' presents in the function
    if "x" not in inp:
        inp = f"({inp})*(x**0)"
    # Return a function to be used for y value calculation.
    def func(x):
        return eval(inp)
    return func


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(QSize(800, 600))
        # Input Layout Components
        self.input_layout = QHBoxLayout()
        self.function_input = QLineEdit("")
        self.button_to_conv = QPushButton("Plot")
        self.input_layout.setAlignment(Qt.AlignTop)
        self.input_layout.addWidget(self.function_input)
        self.input_layout.addWidget(self.button_to_conv)
        # Range Layout Components
        self.range_layout = QHBoxLayout()
        self.min_input = QDoubleSpinBox()
        self.min_input.setPrefix("Min value: ")
        self.min_input.setRange(-3000, 3000)
        self.min_input.setValue(-5)
        self.max_input = QDoubleSpinBox()
        self.max_input.setPrefix("Max value: ")
        self.max_input.setRange(-3000, 3000)
        self.max_input.setValue(5)
        self.range_layout.setAlignment(Qt.AlignTop)
        self.range_layout.addWidget(self.min_input)
        self.range_layout.addWidget(self.max_input)
        # Matplotlib figure (Plot)
        self.canvas = FigureCanvas(Figure(figsize=(8,8)))
        self.ax = self.canvas.figure.subplots()
        self.ax.set_xlabel("X-Axis")
        self.ax.set_ylabel("Y-Axis")
        self.ax.grid()
        # Main Layout Grouper
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.range_layout)
        self.main_layout.addWidget(self.canvas)
        # Error Message Box Layout
        self.err_msg = QMessageBox()
        self.err_msg.setStyleSheet("QLabel{color:red}")
        # Other properties will be adjusted depending on \
        # the error type.
        # Logic Wrapper
        self.button_to_conv.clicked.connect(lambda _: self.plotter(None))
        self.min_input.valueChanged.connect(lambda _: self.plotter("min"))
        self.max_input.valueChanged.connect(lambda _: self.plotter("max"))
        # Load main layout
        self.setLayout(self.main_layout)
    
    def plotter(self, event):
        """Function update for the displated plot."""
        min_val = self.min_input.value()
        max_val = self.max_input.value()
        # Validate Range
        if min_val >= max_val and event == "min":
            self.err_msg.setWindowTitle("Range Error!")
            self.err_msg.setText("Minimum input must be less than Maximum input")
            self.err_msg.show()
            self.min_input.setValue( max_val-1 )
        elif max_val <= min_val and event == "max":
            self.err_msg.setWindowTitle("Range Error!")
            self.err_msg.setText("Maximum input must be bigger than Minimum input")
            self.err_msg.show()
            self.max_input.setValue( min_val+1 )
        else:    
            # Create required range
            x = np.linspace(min_val, max_val)
            try:
                y = in2func(self.function_input.text()) (x)
            except ValueError as err:
                self.err_msg.setWindowTitle("Function Error!")
                self.err_msg.setText(str(err))
                self.err_msg.show()
                return
            # Update plot
            self.ax.clear()
            self.ax.plot(x, y)
            self.ax.grid()
            self.canvas.draw()
    # End def
# End Class


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
