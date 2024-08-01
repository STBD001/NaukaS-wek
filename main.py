import sys
from PySide6 import QtWidgets
from continuation import InlineTranslation, update_state


class AppWidget(QtWidgets.QWidget):
    def __init__(self, words):
        super().__init__()
        self.words = words
        self.state = {}
        self.layout = self.initializeLayout()
        self.setLayout(self.layout)

    def initializeLayout(self):
        grid = QtWidgets.QGridLayout()
        row = 0

        for key, correct_translation in self.words.items():
            label = QtWidgets.QLabel(key)
            line_edit = QtWidgets.QLineEdit()
            self.state[key] = InlineTranslation(key, '', '', correct_translation)
            self.state[key].line_edit = line_edit
            line_edit.textChanged.connect(self.createTextChangeHandler(line_edit))
            grid.addWidget(label, row, 0)
            grid.addWidget(line_edit, row, 1)
            row += 1

        return grid

    def createTextChangeHandler(self, line_edit):
        def handleTextChanged():
            update_state(self.state, line_edit)

        return handleTextChanged


if __name__ == '__main__':
    words = {
        'bambino': 'kid',
        'ciao': 'hello',
        'cercare': 'looking for',
        'difficile': 'difficult'
    }
    app = QtWidgets.QApplication([])
    appWidget = AppWidget(words)
    appWidget.resize(800, 600)
    appWidget.setWindowTitle("Aplikacja do nauki języków")
    appWidget.show()
    sys.exit(app.exec_())
