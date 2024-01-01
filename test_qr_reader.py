import usb.core
idVendor = 0x1a86
idProduct = 0xe026

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
    sys.exit(1)

# Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
usb.util.claim_interface(device, 0)

# Write commands to ADU
bytes_written = write_to_adu(device, 'SK0') # set relay 0
bytes_written = write_to_adu(device, 'RK0') # reset relay 0


# Read from the ADU
bytes_written = write_to_adu(device, 'RPA') # request the value of PORT A in binary 

data = read_from_adu(device, 200) # read from device with a 200 millisecond timeout

if data != None:
    print("Received string: {}".format(data))
    print("Received data as int: {}".format(int(data))) # the returned value is a string - we can convert it to a number (int) if we wish

usb.util.release_interface(device, 0)
device.close()