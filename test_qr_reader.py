import usb.core
import usb.util

def find_device(vendor_id, product_id):
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if device is None:
        raise ValueError("Device not found")
    return device

def find_interface_and_endpoint(device):
    for config in device:
        for interface in config:
            for endpoint in interface:
                if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_IN:
                    return interface.bInterfaceNumber, endpoint.bEndpointAddress

    raise ValueError("Could not find a suitable interface and endpoint")

def read_usb_data(device, interface, endpoint, buffer_size=64):
    # Attempt to claim the interface
    try:
        usb.util.claim_interface(device, interface)
    except usb.core.USBError as e:
        if "Resource busy" in str(e):
            print("Interface already claimed by another process or driver.")
            return

    try:
        data = device.read(endpoint, buffer_size)
        print(f"Read data: {data}")
    finally:
        usb.util.release_interface(device, interface)

if __name__ == "__main__":
    vendor_id = 0x1a86
    product_id = 0xe026

    usb_device = find_device(vendor_id, product_id)
    interface, endpoint = find_interface_and_endpoint(usb_device)
    read_usb_data(usb_device, interface, endpoint)
