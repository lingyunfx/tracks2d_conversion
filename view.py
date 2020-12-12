from PySide2 import QtWidgets, QtCore


class ConversionView(QtWidgets.QWidget):

    def __init__(self):
        super(ConversionView, self).__init__()
        main_la = QtWidgets.QVBoxLayout()
        path_la = QtWidgets.QHBoxLayout()
        input_la = QtWidgets.QHBoxLayout()
        select_la = QtWidgets.QHBoxLayout()
        button_la = QtWidgets.QHBoxLayout()

        path_label = QtWidgets.QLabel('Source Path:')
        self.path_input = QtWidgets.QLineEdit()
        self.path_bt = QtWidgets.QPushButton('..')
        self.path_bt.setFixedWidth(60)

        x_res_label = QtWidgets.QLabel('Width:')
        y_res_label = QtWidgets.QLabel('Height: ')
        offset_label = QtWidgets.QLabel('Offset: ')
        rename_label = QtWidgets.QLabel('Rename: ')
        self.x_res_input = QtWidgets.QLineEdit('1920')
        self.y_res_input = QtWidgets.QLineEdit('1080')
        self.offset_input = QtWidgets.QLineEdit('0')
        self.rename_input = QtWidgets.QLineEdit()

        from_label = QtWidgets.QLabel('From: ')
        from_label.setFixedWidth(50)
        to_label = QtWidgets.QLabel('To:')
        to_label.setFixedWidth(30)
        self.from_select = QtWidgets.QComboBox()
        self.from_select.setFixedWidth(150)
        self.to_select = QtWidgets.QComboBox()
        self.to_select.setFixedWidth(150)
        select_la.setAlignment(QtCore.Qt.AlignLeft)

        self.ok_button = QtWidgets.QPushButton('Ok')
        self.cancel_button = QtWidgets.QPushButton('Cancel')

        for widget in [path_label, self.path_input, self.path_bt]:
            path_la.addWidget(widget)

        for widget in [x_res_label, self.x_res_input, y_res_label, self.y_res_input,
                       offset_label, self.offset_input, rename_label, self.rename_input]:
            input_la.addWidget(widget)

        for widget in [from_label, self.from_select, to_label, self.to_select]:
            select_la.addWidget(widget)

        for widget in [self.ok_button, self.cancel_button]:
            button_la.addWidget(widget)

        select_list = ['SynthEyes', '3DEqualizer', 'PFtrack', 'Boujou']
        self.from_select.addItems(select_list)
        self.to_select.addItems(select_list)
        self.to_select.setCurrentIndex(1)

        main_la.addLayout(path_la)
        main_la.addLayout(input_la)
        main_la.addLayout(select_la)
        main_la.addLayout(button_la)
        self.setLayout(main_la)
        self.setMinimumWidth(500)


def show_ui():
    global locater
    locater = ConversionView()
    locater.show()





