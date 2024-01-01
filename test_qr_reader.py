import os
#os.environ['PYUSB_DEBUG'] = 'debug' # uncomment for verbose pyusb output
import sys
import platform
import usb.core
import usb.backend.libusb1

VENDOR_ID = 0x1a86
PRODUCT_ID = 0xe026

def write_to_adu(dev, msg_str):
    print("Writing command: {}".format(msg_str))
    # message structure:
    #   message is an ASCII string containing the command
    #   8 bytes in lenth
    #   0th byte must always be 0x01
    #   bytes 1 to 7 are ASCII character values representing the command
    #   remainder of message is padded to character code 0 (null)
    byte_str = chr(0x01) + msg_str + chr(0) * max(7 - len(msg_str), 0)

    num_bytes_written = 0

    try:
        num_bytes_written = dev.write(0x01, byte_str)
    except usb.core.USBError as e:
        print (e.args)

    return num_bytes_written

def read_from_adu(dev, timeout):
    try:
        data = dev.read(0x81, 64, timeout)
    except usb.core.USBError as e:
        print ("Error reading response: {}".format(e.args))
        return None

    byte_str = ''.join(chr(n) for n in data[1:]) # construct a string out of the read values, starting from the 2nd byte
    result_str = byte_str.split('\x00',1)[0] # remove the trailing null '\x00' characters

    if len(result_str) == 0:
        return None

    return result_str

if __name__ == "__main__":

    was_kernel_driver_active = False
    device = None

    device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

    # if the OS kernel already claimed the device
    if device.is_kernel_driver_active(0) is True:
        # tell the kernel to detach
        device.detach_kernel_driver(0)
        was_kernel_driver_active = True
    else:
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

    if device is None:
        raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
        sys.exit(1)

    device.reset()

    # Set the active configuration. With no arguments, the first configuration will be the active one
    device.set_configuration()

    # Claim interface 0
    usb.util.claim_interface(device, 0)

    # Write commands to ADU
    # bytes_written = write_to_adu(device, 'SK0') # set relay 0
    # bytes_written = write_to_adu(device, 'RK0') # reset relay 0

    # Read from the ADU
    bytes_written = write_to_adu(device, 'RPA') # request the value of PORT A in binary 
    data = read_from_adu(device, 200) # read from device with a 200 millisecond timeout

    if data != None:
        print("Received string: {}".format(data))
        print("Received data as int: {}".format(int(data)))

    usb.util.release_interface(device, 0)

    # This applies to Linux only - reattach the kernel driver if we previously detached it
    if was_kernel_driver_active == True:
        device.attach_kernel_driver(0)
