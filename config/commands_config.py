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

DEVICE_LIST = [
    "ESP32S2 Dev Module",
    "DOIT ESP32 DEVKIT V1",
    "WEMOS D1 MINI"
]

COMMANDS_CONFIG = {
    "GPIO_OUTPUT": {
        "id": {
            DEVICE_LIST[0] : [33, 34, 35, 36, 37, 38],
            DEVICE_LIST[1] : [4, 14, 16, 17, 27],
            DEVICE_LIST[2] : [13, 14, 15]
        },
        "validator": None
    },
    "GPIO_INPUT": {
        "id": {
            DEVICE_LIST[0] : [10, 11, 12, 13],
            DEVICE_LIST[1] : [35, 36, 39],
            DEVICE_LIST[2] : [16, 17]
        },
        "validator": None
    },
    "PWM_OUTPUT": {
        "id": {
            DEVICE_LIST[0] : [14, 15, 16],
            DEVICE_LIST[1] : [5, 18, 19],
            DEVICE_LIST[2] : [0, 2, 4]
        },
        "validator": None
    },
    "ADC_INPUT": {
        "id": {
            DEVICE_LIST[0] : [3, 4, 5, 6, 7],
            DEVICE_LIST[1] : [34, 13, 15],
            DEVICE_LIST[2] : [34, 35, 36, 39]
        },
        "validator": None
    },
    "DAC_OUTPUT": {
        "id": {
            DEVICE_LIST[0] : [18, 100, 101, 102, 103],
            DEVICE_LIST[1] : [25, 100, 101, 102, 103],
            DEVICE_LIST[2] : [100, 101, 102, 103]
        },
        "validator": None
    },
    "GEN_SIGNAL": {
        "id": {
            DEVICE_LIST[0] : [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            DEVICE_LIST[1] : [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            DEVICE_LIST[2] : [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS]
        },
        "validator": None
    },
    "CLOSED_LOOP": {
        "id": {
            DEVICE_LIST[0] : [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            DEVICE_LIST[1] : [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            DEVICE_LIST[2] : [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS]
        },
        "validator": None
    }
}