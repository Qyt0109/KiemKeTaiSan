import usb.core
idVendor = 0x1a86
idProduct = 0xe026
dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active():
    dev.detach_kernel_driver()

dev.set_configuration()
eadd = ep.bEndpointAddress

r = dev.read(eadd, 1024)
print(len(r))
print(r)