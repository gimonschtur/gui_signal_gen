# ESP32 Automation System Command Configuration

from enum import Enum, auto

class SIGNAL_GEN_PARAMS(Enum):
    """
    Enum for signal generation parameters.
    """
    SIGNAL_GEN_AMPLITUDE_V  = auto()
    SIGNAL_GEN_FREQUENCY_HZ = auto()

class CLOSED_LOOP_PARAMS(Enum):
    """
    Enum for closed loop parameters.
    """
    CONFIG_MAX_VAL           = auto()
    CONFIG_INIT_VAL          = auto()
    CONFIG_CAPPED_VAL        = auto()
    CONFIG_INCR_VAL          = auto()
    CONFIG_DECAY_VAL         = auto()
    CONFIG_DECAY_INTERVAL_MS = auto()
    CONFIG_DEBUG             = auto()
    CONFIG_DAC1_ENABLED      = auto()
    CONFIG_DAC2_ENABLED      = auto()
    CONFIG_SENSOR_TYPE       = auto()
    CONFIG_PRINT_VAL         = auto()
    CONFIG_OVERRIDE_DAC1_VAL = auto()
    CONFIG_OVERRIDE_DAC2_VAL = auto()
    CONFIG_NUM_FIELDS        = auto()

COMMANDS_CONFIG = {
    "GPIO_OUTPUT": {
        "id": {
            "ESP32S2 Dev Module"  : [33, 34, 35, 36, 37, 38],
            "DOIT ESP32 DEVKIT V1": [4, 14, 16, 17, 27],
            "WEMOS D1 MINI"       : [13, 14, 15]
        },
        "validator": None
    },
    "GPIO_INPUT": {
        "id": {
            "ESP32S2 Dev Module"  : [10, 11, 12, 13],
            "DOIT ESP32 DEVKIT V1": [35, 36, 39],
            "WEMOS D1 MINI"       : [16, 17]
        },
        "validator": None
    },
    "PWM_OUTPUT": {
        "id": {
            "ESP32S2 Dev Module"  : [14, 15, 16],
            "DOIT ESP32 DEVKIT V1": [5, 18, 19],
            "WEMOS D1 MINI"       : [0, 2, 4]
        },
        "validator": None
    },
    "ADC_INPUT": {
        "id": {
            "ESP32S2 Dev Module"  : [3, 4, 5, 6, 7],
            "DOIT ESP32 DEVKIT V1": [34, 13, 15],
            "WEMOS D1 MINI"       : [34, 35, 36, 39]
        },
        "validator": None
    },
    "DAC_OUTPUT": {
        "id": {
            "ESP32S2 Dev Module"  : [18, 100, 101, 102, 103],
            "DOIT ESP32 DEVKIT V1": [25, 100, 101, 102, 103],
            "WEMOS D1 MINI"       : [100, 101, 102, 103]
        },
        "validator": None
    },
    "GEN_SIGNAL": {
        "id": {
            "ESP32S2 Dev Module"  : [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            "DOIT ESP32 DEVKIT V1": [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            "WEMOS D1 MINI"       : [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS]
        },
        "validator": None
    },
    "CLOSED_LOOP": {
        "id": {
            "ESP32S2 Dev Module"  : [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            "DOIT ESP32 DEVKIT V1": [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            "WEMOS D1 MINI"       : [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS]
        },
        "validator": None
    }
}