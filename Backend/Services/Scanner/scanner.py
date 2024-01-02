# git clone https://github.com/vpatron/barcode_scanner_python.git

import evdev
import logging

ERROR_CHARACTER = '?'
VALUE_UP = 0
VALUE_DOWN = 1
CHARMAP = {
        evdev.ecodes.KEY_1: ['1', '!'],
        evdev.ecodes.KEY_2: ['2', '@'],
        evdev.ecodes.KEY_3: ['3', '#'],
        evdev.ecodes.KEY_4: ['4', '$'],
        evdev.ecodes.KEY_5: ['5', '%'],
        evdev.ecodes.KEY_6: ['6', '^'],
        evdev.ecodes.KEY_7: ['7', '&'],
        evdev.ecodes.KEY_8: ['8', '*'],
        evdev.ecodes.KEY_9: ['9', '('],
        evdev.ecodes.KEY_0: ['0', ')'],
        evdev.ecodes.KEY_MINUS: ['-', '_'],
        evdev.ecodes.KEY_EQUAL: ['=', '+'],
        evdev.ecodes.KEY_TAB: ['\t', '\t'],
        evdev.ecodes.KEY_Q: ['q', 'Q'],
        evdev.ecodes.KEY_W: ['w', 'W'],
        evdev.ecodes.KEY_E: ['e', 'E'],
        evdev.ecodes.KEY_R: ['r', 'R'],
        evdev.ecodes.KEY_T: ['t', 'T'],
        evdev.ecodes.KEY_Y: ['y', 'Y'],
        evdev.ecodes.KEY_U: ['u', 'U'],
        evdev.ecodes.KEY_I: ['i', 'I'],
        evdev.ecodes.KEY_O: ['o', 'O'],
        evdev.ecodes.KEY_P: ['p', 'P'],
        evdev.ecodes.KEY_LEFTBRACE: ['[', '{'],
        evdev.ecodes.KEY_RIGHTBRACE: [']', '}'],
        evdev.ecodes.KEY_A: ['a', 'A'],
        evdev.ecodes.KEY_S: ['s', 'S'],
        evdev.ecodes.KEY_D: ['d', 'D'],
        evdev.ecodes.KEY_F: ['f', 'F'],
        evdev.ecodes.KEY_G: ['g', 'G'],
        evdev.ecodes.KEY_H: ['h', 'H'],
        evdev.ecodes.KEY_J: ['j', 'J'],
        evdev.ecodes.KEY_K: ['k', 'K'],
        evdev.ecodes.KEY_L: ['l', 'L'],
        evdev.ecodes.KEY_SEMICOLON: [';', ':'],
        evdev.ecodes.KEY_APOSTROPHE: ['\'', '"'],
        evdev.ecodes.KEY_BACKSLASH: ['\\', '|'],
        evdev.ecodes.KEY_Z: ['z', 'Z'],
        evdev.ecodes.KEY_X: ['x', 'X'],
        evdev.ecodes.KEY_C: ['c', 'C'],
        evdev.ecodes.KEY_V: ['v', 'V'],
        evdev.ecodes.KEY_B: ['b', 'B'],
        evdev.ecodes.KEY_N: ['n', 'N'],
        evdev.ecodes.KEY_M: ['m', 'M'],
        evdev.ecodes.KEY_COMMA: [',', '<'],
        evdev.ecodes.KEY_DOT: ['.', '>'],
        evdev.ecodes.KEY_SLASH: ['/', '?'],
        evdev.ecodes.KEY_SPACE: [' ', ' ']
        }

class Scanner:
    def __init__(self, vendor_id=None, product_id=None) -> None:
        self.device = self.set_device(vendor_id, product_id) if vendor_id and product_id else None

    def set_device(self, vendor_id, product_id):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if device.info.vendor == vendor_id and device.info.product == product_id:
                print(f"Device found: info={device.info}, path={device.path}, name={device.name}, phys={device.phys}")
                return device
        print("Device not found!")
        return None
    
    def read_barcode(self):
        if self.device:
            try:
                self.device.grab()
                print("Start scanning from device")
                scanned_string = ''
                shift_active = False
                for event in self.device.read_loop():
                    if event.code == evdev.ecodes.KEY_ENTER and event.value == VALUE_DOWN:
                        return scanned_string
                    elif event.code == evdev.ecodes.KEY_LEFTSHIFT or event.code == evdev.ecodes.KEY_RIGHTSHIFT:
                        shift_active = event.value == VALUE_DOWN
                    elif event.value == VALUE_DOWN:
                        ch = CHARMAP.get(event.code, ERROR_CHARACTER)[1 if shift_active else 0]
                        scanned_string += ch
                self.device.ungrab()
                return scanned_string
            except Exception as err:
                logging.error(err)
                return None
        else:
            print("No device avaiable")
            return None

""" Example useagetest.py
from Backend.Services.Scanner.scanner import Scanner

if __name__ == "__main__":
    vendor_id = 0x1a86
    product_id = 0xe026
    scanner = Scanner(vendor_id=vendor_id, product_id=product_id)
    barcode = scanner.read_barcode()
    print(barcode)
"""