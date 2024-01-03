# Fake scanner for testing and developing
class Scanner:
    def __init__(self, vendor_id=None, product_id=None) -> None:
        self.device = "Fake device" if vendor_id and product_id else None

    def set_device(self, vendor_id, product_id):
        pass
    
    def read_barcode(self, fake_barcode=None):
        return fake_barcode