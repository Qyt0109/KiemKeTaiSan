import usb.core
import usb.util

def find_device(vendor_id, product_id):
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if device is None:
        raise ValueError("Device not found")
    return device

def find_interface_and_endpoint(device):
    # Iterate over configurations
    for config in device:
        # Iterate over interfaces in the configuration
        for interface in config:
            # Iterate over endpoints in the interface
            for endpoint in interface:
                # Check if the endpoint is an IN endpoint (data flowing into the host)
                if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_IN:
                    return interface.bInterfaceNumber, endpoint.bEndpointAddress

    raise ValueError("Could not find a suitable interface and endpoint")

def read_usb_data(device, interface, endpoint, buffer_size=64):
    # Claim the interface
    usb.util.claim_interface(device, interface)

    try:
        # Read data from the USB device
        data = device.read(endpoint, buffer_size)
        print(f"Read data: {data}")
    finally:
        # Release the interface
        usb.util.release_interface(device, interface)

if __name__ == "__main__":
    vendor_id = 0x1a86  # Replace with your USB device's vendor ID
    product_id = 0xe026  # Replace with your USB device's product ID

    usb_device = find_device(vendor_id, product_id)

    # Find interface and endpoint
    interface, endpoint = find_interface_and_endpoint(usb_device)

    # Read USB data
    read_usb_data(usb_device, interface, endpoint)
