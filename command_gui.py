import sys
import warnings
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel,
                            QGroupBox, QGridLayout)
from config.commands_config import COMMANDS_CONFIG, DEVICE_LIST

# Filter out specifically the sipPyTypeDict deprecation warning
warnings.filterwarnings('ignore', message='.*sipPyTypeDict.*')

class CommandGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Commands")
        self.current_board = DEVICE_LIST[1]  # Default board
        self.initUI()

    def initUI(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create group box for commands
        group_box = QGroupBox("Custom Commands")
        main_layout.addWidget(group_box)

        # Create layout for group box
        group_layout = QVBoxLayout()
        group_box.setLayout(group_layout)

        # Create grid layout for command inputs
        command_grid_layout = QGridLayout()

        device_layout = QHBoxLayout()
        device_label = QLabel("Device:")
        self.device_combo = QComboBox()
        self.device_combo.setFixedWidth(200)
        self.device_combo.addItems(DEVICE_LIST)
        self.device_combo.setCurrentText(self.current_board)
        self.device_combo.currentTextChanged.connect(self.update_current_device)
        device_layout.addWidget(device_label)
        device_layout.addWidget(self.device_combo)

        group_layout.addLayout(device_layout)

        # Command ComboBox
        self.command_combo = QComboBox()
        self.command_combo.setFixedWidth(200)
        self.command_combo.addItems(COMMANDS_CONFIG.keys())
        self.command_combo.currentTextChanged.connect(self.update_id_combo)

        # ID ComboBox
        self.id_combo = QComboBox()
        self.id_combo.setFixedWidth(200)

        # Value input
        self.value_input = QLineEdit()

        command_grid_layout.addWidget(QLabel("Command"),  0, 0)
        command_grid_layout.addWidget(QLabel("ID"),       0, 1)
        command_grid_layout.addWidget(QLabel("VALUE"),    0, 2)

        command_grid_layout.addWidget(self.command_combo, 1, 0)
        command_grid_layout.addWidget(self.id_combo,      1, 1)
        command_grid_layout.addWidget(self.value_input,   1, 2)

        # Add command grid layout to group layout
        group_layout.addLayout(command_grid_layout)

        # Create button and response layout
        button_layout = QVBoxLayout()

        # Send Command button
        send_button = QPushButton("Send Command")
        send_button.clicked.connect(self.send_command)

        # Command output field
        self.command_output_field = QLineEdit()
        self.command_output_field.setReadOnly(True)
        self.command_output_field.setPlaceholderText("COMMAND OUTPUT")

        # Response field
        self.response_field = QLineEdit()
        self.response_field.setReadOnly(True)
        self.response_field.setPlaceholderText("RESPONSE")

        # Add widgets to button layout
        button_layout.addWidget(send_button)
        button_layout.addWidget(self.command_output_field)
        button_layout.addWidget(self.response_field)

        # Add button layout to group layout
        group_layout.addLayout(button_layout)

        # Initialize the ID combo box
        self.update_id_combo()

    def update_current_device(self):
        self.current_board = self.device_combo.currentText()
        self.update_id_combo()

    def update_id_combo(self):
        """Update the ID combo box based on the selected command"""
        self.id_combo.clear()
        selected_command = self.command_combo.currentText()
        if selected_command in COMMANDS_CONFIG:
            ids = COMMANDS_CONFIG[selected_command]["id"][self.current_board]
            self.id_combo.addItems([str(id_) for id_ in ids])

    def send_command(self):
        """Handle the send command button click"""
        command = self.command_combo.currentText()
        id_value = self.id_combo.currentText()
        value = self.value_input.text()

        self.command_output_field.clear()
        self.response_field.clear()

        if all([command, id_value, value]):
            # Here you would typically send the command to the ESP32
            # For now, we'll just show the command in the response field
            command = f"{command} {id_value} {value}"
            self.command_output_field.setText(command)

def main():
    app = QApplication(sys.argv)
    gui = CommandGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
