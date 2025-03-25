# ESP32 Automation System Command Configuration

from enum import Enum, auto
from utils.validators import RangeIntValidator

class COMMANDS(Enum):
    """
    Enum for commands.
    """
    GPIO_OUTPUT = auto()
    GPIO_INPUT  = auto()
    PWM_OUTPUT  = auto()
    ADC_INPUT   = auto()
    DAC_OUTPUT  = auto()
    GEN_SIGNAL  = auto()
    CLOSED_LOOP = auto()

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

# Define the range for each command
VALIDATOR_RANGES = {
    COMMANDS.GPIO_OUTPUT.name: (0, 10000),
    COMMANDS.GPIO_INPUT.name : (0, 10000),
    COMMANDS.PWM_OUTPUT.name : (0, 10000),
    COMMANDS.ADC_INPUT.name  : (0, 0),
    COMMANDS.DAC_OUTPUT.name : (0, 10000),
    COMMANDS.GEN_SIGNAL.name : (0, 10000),
    COMMANDS.CLOSED_LOOP.name: (0, 10000)
}

COMMANDS_CONFIG = {
    COMMANDS.GPIO_OUTPUT.name: {
        "id": {
            DEVICE_LIST[0]: [33, 34, 35, 36, 37, 38],
            DEVICE_LIST[1]: [4, 14, 16, 17, 27],
            DEVICE_LIST[2]: [13, 14, 15]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.GPIO_OUTPUT.name])
    },
    COMMANDS.GPIO_INPUT.name: {
        "id": {
            DEVICE_LIST[0]: [10, 11, 12, 13],
            DEVICE_LIST[1]: [35, 36, 39],
            DEVICE_LIST[2]: [16, 17]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.GPIO_INPUT.name])
    },
    COMMANDS.PWM_OUTPUT.name: {
        "id": {
            DEVICE_LIST[0]: [14, 15, 16],
            DEVICE_LIST[1]: [5, 18, 19],
            DEVICE_LIST[2]: [0, 2, 4]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.PWM_OUTPUT.name])
    },
    COMMANDS.ADC_INPUT.name: {
        "id": {
            DEVICE_LIST[0]: [3, 4, 5, 6, 7],
            DEVICE_LIST[1]: [34, 13, 15],
            DEVICE_LIST[2]: [34, 35, 36, 39]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.ADC_INPUT.name])
    },
    COMMANDS.DAC_OUTPUT.name: {
        "id": {
            DEVICE_LIST[0]: [18, 100, 101, 102, 103],
            DEVICE_LIST[1]: [25, 100, 101, 102, 103],
            DEVICE_LIST[2]: [100, 101, 102, 103]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.DAC_OUTPUT.name])
    },
    COMMANDS.GEN_SIGNAL.name: {
        "id": {
            DEVICE_LIST[0]: [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            DEVICE_LIST[1]: [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS],
            DEVICE_LIST[2]: [param.name.replace("SIGNAL_GEN_", " ") for param in SIGNAL_GEN_PARAMS]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.GEN_SIGNAL.name])
    },
    COMMANDS.CLOSED_LOOP.name: {
        "id": {
            DEVICE_LIST[0]: [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            DEVICE_LIST[1]: [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS],
            DEVICE_LIST[2]: [param.name.replace("CONFIG_", " ") for param in CLOSED_LOOP_PARAMS]
        },
        "validator": RangeIntValidator(*VALIDATOR_RANGES[COMMANDS.CLOSED_LOOP.name])
    }
}