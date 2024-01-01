import usb.core
import sys

dev = usb.core.find(idVendor=0x1a86,
                    idProduct=0xe026)
ep = dev[0].interfaces()[5].endpoints()[0]

i = dev[0].interfaces()[5].bInterfaceNumber

dev.reset()

if dev.is_kernel_driver_active(i):
    try:
        dev.detach_kernel_driver(i)
    except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))
    
dev.set_configuration()

eaddr = ep.bEndpointAdress

r = dev.read(eaddr,1024)
print(len(r))