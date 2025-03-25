import sys
import warnings
import logging
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel,
                            QGroupBox, QGridLayout, QFormLayout)
from config.commands_config import COMMANDS_CONFIG, DEVICE_LIST, COMMANDS
from imports.serial_commander.serial_communication import SerialCommunication

# Filter out specifically the sipPyTypeDict deprecation warning
warnings.filterwarnings('ignore', message='.*sipPyTypeDict.*')

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

class CommandGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Commands")
        self.logger = logging.getLogger(__name__)
        self.current_board = DEVICE_LIST[1]  # Default board
        self.serial_comm = SerialCommunication()

        # List available COM ports
        self.available_ports = self.serial_comm.list_available_ports()

        self.logger.info("Command GUI initialized.")

        self.initUI()

    def create_serial_comm_group_box(self) -> QGroupBox:
        group_box = QGroupBox("Serial Communication")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        serial_layout = QHBoxLayout()
        layout.addLayout(serial_layout)

        self.port_combo = QComboBox()
        self.port_combo.addItems(self.available_ports)

        port_list_form_layout = QFormLayout()
        port_list_form_layout.addRow("Port:", self.port_combo)

        port_connection_button = QPushButton("Connect")
        port_connection_button.clicked.connect(self.connect_port)

        serial_layout.addLayout(port_list_form_layout)
        serial_layout.addWidget(port_connection_button)

        return group_box

    def create_command_group_box(self) -> QGroupBox:
        group_box = QGroupBox("Custom Commands")

        # Create layout for group box
        command_group_layout = QVBoxLayout()
        group_box.setLayout(command_group_layout)

        # Create grid layout for command inputs
        command_grid_layout = QGridLayout()

        device_layout = QFormLayout()
        self.device_combo = QComboBox()
        self.device_combo.setFixedWidth(200)
        self.device_combo.addItems(DEVICE_LIST)
        self.device_combo.setCurrentText(self.current_board)
        self.device_combo.currentTextChanged.connect(self.update_current_device)
        device_layout.addRow("Device:", self.device_combo)

        command_group_layout.addLayout(device_layout)

        # Command ComboBox
        self.command_combo = QComboBox()
        self.command_combo.setFixedWidth(200)
        self.command_combo.addItems(COMMANDS_CONFIG.keys())
        self.command_combo.currentTextChanged.connect(self.update_command_combo)

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
        command_group_layout.addLayout(command_grid_layout)

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
        command_group_layout.addLayout(button_layout)

        return group_box

    def initUI(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        main_layout.addWidget(self.create_serial_comm_group_box())
        main_layout.addWidget(self.create_command_group_box())

        # Initialize the ID combo box
        self.update_id_combo()

    def update_current_device(self):
        self.current_board = self.device_combo.currentText()
        self.update_id_combo()

    def update_command_combo(self):
        if self.command_combo.currentText() == COMMANDS.ADC_INPUT.name:
            self.value_input.setEnabled(False)
            self.value_input.clear()
        else:
            self.value_input.setEnabled(True)

        # Update the ID combo box
        self.update_id_combo()

    def update_id_combo(self):
        """Update the ID combo box based on the selected command"""
        self.id_combo.clear()
        selected_command = self.command_combo.currentText()
        if selected_command in COMMANDS_CONFIG:
            ids = COMMANDS_CONFIG[selected_command]["id"][self.current_board]
            self.id_combo.addItems([str(id_) for id_ in ids])

            # Set the validator for the value input
            validator = COMMANDS_CONFIG[selected_command]["validator"]
            self.value_input.setValidator(validator)

    def send_command(self):
        """Handle the send command button click"""
        command = self.command_combo.currentText()
        id_value = self.id_combo.currentText()
        value = self.value_input.text()

        self.command_output_field.clear()
        self.response_field.clear()

        # Handle ADC_INPUT command separately
        if command == COMMANDS.ADC_INPUT.name:
            formatted_command = self.format_command(command, id_value)
            self.command_output_field.setText(formatted_command)
            return

        # Check if all required fields are filled
        if not all([command, id_value, value]):
            return  # Early return if any field is empty

        # Format and display the command
        formatted_command = self.format_command(command, id_value, value)
        self.command_output_field.setText(formatted_command)

    def format_command(self, command, id_value, value=None):
        """Format the command string based on the inputs"""
        if value is not None:
            return f"{command} {id_value} {value}"
        return f"{command} {id_value}"

    def connect_port(self):
        port = self.port_combo.currentText()
        self.serial_comm.open_serial(port)

def main():
    app = QApplication(sys.argv)
    gui = CommandGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
