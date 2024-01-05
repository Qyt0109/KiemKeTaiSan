from Backend.Database.db_sessions import *

def main():
    phong = CRUD_Phong.read(phong_id=2)
    if not phong:
        return
    handler_kiem_ke = Handler_KiemKe(phong.id)
    handler_kiem_ke.add_tai_san(tai_san_id=10, trang_thai=BanGhiKiemKeState.IS_AVAILABLE.value)
    handler_kiem_ke.add_tai_san(tai_san_id=14, trang_thai=BanGhiKiemKeState.NEW_INCLUDE.value)
    handler_kiem_ke.add_tai_san(tai_san_id=12, trang_thai=BanGhiKiemKeState.NOT_AVAILABLE.value)
    handler_kiem_ke.complete()
if __name__ == "__main__":
    main()