from Backend.Database.db_models import *
from Backend.Database.db_sessions import *

from collections import defaultdict

# Assuming phong is an instance of Phong
phongs = CRUD_Phong.read_all()

# Now you have a nested dictionary where tai_sans_grouped[nhom_tai_san][loai_tai_san] is a list of TaiSans.

# Displaying the grouped TaiSans
for phong in phongs:
    print(f"Ten Phong: {phong.ten}")
    
    tai_sans_grouped = defaultdict(lambda: defaultdict(list))   # Dictionary of dictionaries of lists of tai_san
    for tai_san in phong.tai_sans:
        loai_tai_san = tai_san.loai_tai_san if tai_san.loai_tai_san else None
        nhom_tai_san = loai_tai_san.nhom_tai_san if loai_tai_san else None
        if loai_tai_san and nhom_tai_san:
            tai_sans_grouped[nhom_tai_san][loai_tai_san].append(tai_san)
    for nhom_tai_san, loai_tai_san_dict in tai_sans_grouped.items():
        # Nhom tai san
        print(f"Nhom tai san: {nhom_tai_san.ten}")

        for loai_tai_san, tai_san_list in loai_tai_san_dict.items():
            # Loai tai san
            print(f"    Loai tai san: {loai_tai_san.ten}")

            for tai_san in tai_san_list:
                # Tai san
                print(f"        Tai san: {tai_san.mo_ta}")