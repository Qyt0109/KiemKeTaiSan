from Backend.Database.db_models import *
from Backend.Database.db_sessions import *

# ... (your existing code)
"""
lich_su_kiem_ke = LichSuKiemKe(phong_id=2)
session.add(lich_su_kiem_ke)

# Thêm bản ghi kiểm kê
ban_ghi_kiem_ke = BanGhiKiemKe(thoi_gian=datetime.utcnow(), lich_su_kiem_ke_id=lich_su_kiem_ke.id)
session.add(ban_ghi_kiem_ke)

# Add tai_san13_phong1 with trang_thai
tai_san13_phong1 = CRUD_TaiSan.read(tai_san_id=13)
trang_thai_tai_san13 = "Your Trang Thai Here"  # Set your trang_thai value
association1 = ban_ghi_kiem_ke_tai_san_association.insert().values(
    tai_san_id=tai_san13_phong1.id,
    ban_ghi_kiem_ke_id=ban_ghi_kiem_ke.id,
    trang_thai=trang_thai_tai_san13
)
session.execute(association1)

# Add tai_san14_phong2 with trang_thai
tai_san14_phong2 = CRUD_TaiSan.read(tai_san_id=14)
trang_thai_tai_san14 = "Your Trang Thai Here"  # Set your trang_thai value
association2 = ban_ghi_kiem_ke_tai_san_association.insert().values(
    tai_san_id=tai_san14_phong2.id,
    ban_ghi_kiem_ke_id=ban_ghi_kiem_ke.id,
    trang_thai=trang_thai_tai_san14
)
session.execute(association2)

# Commit all changes at the end
session.commit()
"""
# Kiểm tra lịch sử kiểm kê và các thông tin liên quan
phong = CRUD_Phong.read(phong_id=2)
print(f"Lịch sử kiểm kê của phòng {phong.ten}:")

for lich_su_kiem_ke in phong.lich_su_kiem_kes:
    print(f"- Thời gian: {lich_su_kiem_ke.thoi_gian}")
    for ban_ghi_kiem_ke in lich_su_kiem_ke.ban_ghi_kiem_kes:
        print(f"  + Thời gian kiểm kê: {ban_ghi_kiem_ke.thoi_gian}")
        for tai_san in ban_ghi_kiem_ke.tai_sans:
            # Access the association attributes to get trang_thai
            trang_thai = session.query(ban_ghi_kiem_ke_tai_san_association.c.trang_thai).filter(
                ban_ghi_kiem_ke_tai_san_association.c.tai_san_id == tai_san.id,
                ban_ghi_kiem_ke_tai_san_association.c.ban_ghi_kiem_ke_id == ban_ghi_kiem_ke.id
            ).scalar()
            
            print(f"    * Tài sản: {tai_san.ma} - {tai_san.mo_ta} - {tai_san.phong.id}")
            print(f"      + Trạng thái: {trang_thai}")

