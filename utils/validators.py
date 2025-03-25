from PyQt5.QtGui import QIntValidator

class RangeIntValidator(QIntValidator):
    def __init__(self, min_value, max_value, parent=None):
        super().__init__(min_value, max_value, parent)