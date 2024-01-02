#!python

# Tested with `SC-8110-2D-B` 1d & 2d barcode scanner
#
# Inspired by https://github.com/julzhk/usb_barcode_scanner
# which was inspired by https://www.piddlerintheroot.com/barcode-scanner/
# https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=55100
# from 'brechmos' - thank-you!
#
# This implementation doesn't directly decode hidraw stream, but uses
# evdev and grabs the device, so the code arrives only in this script
# and not in any active input window.
# 
# Also, it uses a list of USB vendor:product to identify the device,
# so that you don't have to set the dev path.
#
# License: MIT No Attribution License (MIT-0) - https://opensource.org/licenses/MIT-0

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

def read_barcode(device):
    barcode_string_output = ''
    # barcode can have a 'shift' character; this switches the character set
    # from the lower to upper case variant for the next character only.
    shift_active = False
    for event in device.read_loop():
        #print('categorize:', evdev.categorize(event))
        #print('typeof:', type(event.code))
        #print("event.code:", event.code)
        #print("event.type:", event.type)
        #print("event.value:", event.value)
        #print("event:", event)
        if event.code == evdev.ecodes.KEY_ENTER and event.value == VALUE_DOWN:
            #print('KEY_ENTER -> return')
            # all barcodes end with a carriage return
            return barcode_string_output
        elif event.code == evdev.ecodes.KEY_LEFTSHIFT or event.code == evdev.ecodes.KEY_RIGHTSHIFT:
            #print('SHIFT')
            shift_active = event.value == VALUE_DOWN
        elif event.value == VALUE_DOWN:
            ch = CHARMAP.get(event.code, ERROR_CHARACTER)[1 if shift_active else 0]
            #print('ch:', ch)
            # if the charcode isn't recognized, use ?
            barcode_string_output += ch

# lsusb to get VENDOR_ID = 0x1a86 and PRODUCT_ID = 0xe026
# EX: Bus 001 Device 003: ID 1a86:e026 QinHeng Electronics Serial To HID
def get_device(vendor_id, product_id):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        # print('device:', device)
        # print('info:', device.info)
        # print(device.path, device.name, device.phys)
        if device.info.vendor == vendor_id and device.info.product == product_id:
            return device
    return None

if __name__ == '__main__':
    # for path in evdev.list_devices():
    #    print('path:', path)
    vendor_id = 0x1a86
    product_id = 0xe026
    device = get_device(vendor_id, product_id)
    print('selected device:', device)
    device.grab()

    try:
        while True:
            code = read_barcode(device)
            print(code)
    except KeyboardInterrupt:
        logging.debug('Keyboard interrupt')
    except Exception as err:
        logging.error(err)

    device.ungrab()