from Backend.Services.Scanner.scanner import Scanner

if __name__ == "__main__":
    vendor_id = 0x1a86
    product_id = 0xe026
    scanner = Scanner(vendor_id=vendor_id, product_id=product_id)
    barcode = scanner.read_barcode()
    print(barcode)