import usb.core
import usb.util

# Find the USB device by vendor and product ID
vendor_id = 0x1a86  # Replace with your USB device's vendor ID
product_id = 0xe026  # Replace with your USB device's product ID

device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

if device is None:
    raise ValueError("Device not found")

# Set up the USB interface and endpoint
interface = 0  # Replace with the interface number of your USB device
endpoint = 0x81  # Replace with the endpoint address of your USB device

# Claim the interface
usb.util.claim_interface(device, interface)

try:
    # Read data from the USB device
    data = device.read(endpoint, 64)  # Adjust the buffer size as needed

    # Process the read data as needed
    print(f"Read data: {data}")
finally:
    # Release the interface
    usb.util.release_interface(device, interface)
