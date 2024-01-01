import logging

from Backend.Services.QrReader.scanner import barcode_reader

# Bus 001 Device 003: ID 1a86:e026 QinHeng Electronics Serial To HID

if __name__ == "__main__":
    try:
        while True:
            barcode_read = barcode_reader("/dev/hidraw1")
    except KeyboardInterrupt:
        logging.debug("Keyboard interrupt")
    except Exception as err:
        logging.error(err)
