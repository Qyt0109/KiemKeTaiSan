from enum import Enum
from typing import Callable, List, Tuple
from Backend.Database.db_models import *
from Backend.Database.connection_string import connection_string_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an SQLite engine
# echo = True to logging any SQL query to console

engine = create_engine(connection_string_url, echo=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
# default_session = Session()

session = Session()

class CRUD_Status(Enum):
    NOT_FOUND = 'Not Found'
    CREATED = 'Created'
    UPDATED = 'Updated'
    DELETED = 'Deleted'
    ERROR = 'Error'

def crud_handler_wrapper(func: Callable)->Callable:
    def wrapper(*args, **kwargs)->Tuple[CRUD_Status, any]:
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            return CRUD_Status.ERROR
    return wrapper

class CRUD_Khu:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str):
        new_khu = Khu(ten=ten)
        session.add(new_khu)
        return CRUD_Status.CREATED

    @staticmethod
    def read(khu_id: int):
        return session.query(Khu).get(khu_id)
    
    @staticmethod
    def read_all():
        return session.query(Khu).all()

    @staticmethod
    @crud_handler_wrapper
    def update(khu_id: int, new_ten: str=None):
        if new_ten:
            khu = CRUD_Khu.read(khu_id=khu_id)
            if not khu:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                khu.ten = new_ten
            return CRUD_Status.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete(khu_id: int):
        khu = CRUD_Khu.read(khu_id=khu_id)
        if not khu:
            return CRUD_Status.NOT_FOUND
        session.delete(khu)
        return CRUD_Status.DELETED


class CRUD_CanBo:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str, sdt: str=None):
        new_can_bo = CanBo(ten=ten, sdt=sdt)
        session.add(new_can_bo)
        return CRUD_Status.CREATED

    @staticmethod
    def read(can_bo_id: int):
        return session.query(CanBo).get(can_bo_id)
    
    @staticmethod
    def read_all():
        return session.query(CanBo).all()

    @staticmethod
    @crud_handler_wrapper
    def update(can_bo_id: int, new_ten: str=None, new_sdt: str=None):
        if new_ten or new_sdt:
            can_bo = CRUD_CanBo.read(can_bo_id=can_bo_id)
            if not can_bo:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                can_bo.ten = new_ten
            if new_sdt:
                can_bo.sdt = new_sdt
            return CRUD_Status.UPDATED

    @staticmethod
    def delete(can_bo_id: int):
        can_bo = CRUD_CanBo.read(can_bo_id=can_bo_id)
        if not can_bo:
            return CRUD_Status.NOT_FOUND
        session.delete(can_bo)
        return CRUD_Status.DELETED

class CRUD_DonVi:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str, ma:str):
        new_don_vi = DonVi(ten=ten, ma=ma)
        session.add(new_don_vi)
        return CRUD_Status.CREATED

    @staticmethod
    def read(don_vi_id: int):
        return session.query(DonVi).get(don_vi_id)
    
    @staticmethod
    def read_all():
        return session.query(DonVi).all()

    @staticmethod
    def update(don_vi_id: int, new_ten: str=None, new_ma :str=None):
        if new_ten or new_ma:
            don_vi = CRUD_DonVi.read(don_vi_id=don_vi_id)
            if not don_vi:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                don_vi.ten = new_ten
            if new_ma:
                don_vi.ma = new_ma
            return CRUD_Status.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete(don_vi_id: int):
        don_vi = CRUD_DonVi.read(don_vi_id=don_vi_id)
        if not don_vi:
            return CRUD_Status.NOT_FOUND
        session.delete(don_vi)
        return CRUD_Status.DELETED


class CRUD_Phong:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str, ma:str, thong_tin: str=None, khu_id: int=None, don_vi_id: int=None, can_bo_id: int=None):
        new_phong = Phong(ten=ten, ma=ma, thong_tin=thong_tin, khu_id=khu_id, don_vi_id=don_vi_id, can_bo_id=can_bo_id)
        session.add(new_phong)
        return CRUD_Status.CREATED

    @staticmethod
    def read(phong_id: int):
        return session.query(Phong).get(phong_id)
    
    @staticmethod
    def read_all():
        return session.query(Phong).all()

    @staticmethod
    @crud_handler_wrapper
    def update(phong_id: int, new_ten: str=None, new_ma: str=None, new_thong_tin: str=None, new_khu_id: int=None, new_don_vi_id: int=None, new_can_bo_id: int=None):
        if new_ten or new_ma or new_can_bo_id or new_don_vi_id or new_khu_id or new_thong_tin:
            phong = CRUD_Phong.read(phong_id=phong_id)
            if not phong:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                phong.ten = new_ten
            if new_ma:
                phong.ma = new_ma
            if new_thong_tin:
                phong.thong_tin = new_thong_tin
            if new_khu_id:
                phong.khu_id = new_khu_id
            if new_don_vi_id:
                phong.don_vi_id = new_don_vi_id
            if new_can_bo_id:
                phong.can_bo_id = new_can_bo_id
            return CRUD_Status.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete(phong_id: int):
        phong = CRUD_Phong.read(phong_id=phong_id)
        if not phong:
            return CRUD_Status.NOT_FOUND
        session.delete(phong)
        return CRUD_Status.DELETED

class CRUD_NhomTaiSan:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str):
        new_nhom_tai_san = NhomTaiSan(ten=ten)
        session.add(new_nhom_tai_san)
        return CRUD_Status.CREATED

    @staticmethod
    def read(nhom_tai_san_id: int):
        return session.query(NhomTaiSan).get(nhom_tai_san_id)
    
    @staticmethod
    def read_all():
        return session.query(NhomTaiSan).all()

    @staticmethod
    @crud_handler_wrapper
    def update(nhom_tai_san_id: int, new_ten: str=None):
        if new_ten:
            nhom_tai_san = CRUD_NhomTaiSan.read(nhom_tai_san_id=nhom_tai_san_id)
            if not nhom_tai_san:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                nhom_tai_san.ten = new_ten
            return CRUD_Status.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete(nhom_tai_san_id: int):
        nhom_tai_san = CRUD_NhomTaiSan.read(nhom_tai_san_id=nhom_tai_san_id)
        if not nhom_tai_san:
            return CRUD_Status.NOT_FOUND
        session.delete(nhom_tai_san)
        return CRUD_Status.DELETED

class CRUD_LoaiTaiSan:
    @staticmethod
    @crud_handler_wrapper
    def create(ten: str, ma: str, nhom_tai_san_id: int=None):
        new_loai_tai_san = LoaiTaiSan(ten=ten, ma=ma, nhom_tai_san_id=nhom_tai_san_id)
        session.add(new_loai_tai_san)
        return CRUD_Status.CREATED
    
    @staticmethod
    def read(loai_tai_san_id: int):
        return session.query(LoaiTaiSan).get(loai_tai_san_id)

    @staticmethod
    def read_all():
        return session.query(LoaiTaiSan).all()
    
    @staticmethod
    @crud_handler_wrapper
    def update(loai_tai_san_id: int, new_ten: str, new_ma: str, new_nhom_tai_san_id: int=None):
        if new_ten or new_ma or new_nhom_tai_san_id:
            loai_tai_san = CRUD_LoaiTaiSan.read(loai_tai_san_id=loai_tai_san_id)
            if not loai_tai_san:
                return CRUD_Status.NOT_FOUND
            if new_ten:
                loai_tai_san.ten = new_ten
            if new_ma:
                loai_tai_san.ma = new_ma
            if new_nhom_tai_san_id:
                loai_tai_san.nhom_tai_san_id = new_nhom_tai_san_id
            return CRUD_Status.UPDATED

class CRUD_TaiSan:
    @staticmethod
    @crud_handler_wrapper
    def create(ma: str, ma_serial: str=None, mo_ta: str=None, nam_su_dung: str=None, loai_tai_san_id: int=None, phong_id: int=None):
        new_tai_san = TaiSan(ma=ma, ma_serial=ma_serial, mo_ta=mo_ta, nam_su_dung=nam_su_dung, loai_tai_san_id=loai_tai_san_id, phong_id=phong_id)
        session.add(new_tai_san)
        return CRUD_Status.CREATED

    @staticmethod
    def read(tai_san_id: int):
        return session.query(TaiSan).get(tai_san_id)
    
    @staticmethod
    def read_all():
        return session.query(TaiSan).all()

    @staticmethod
    @crud_handler_wrapper
    def update(tai_san_id: int, new_ma: str=None, new_ma_serial: str=None, new_mo_ta: str=None, new_nam_su_dung: str=None, new_loai_tai_san_id: int=None, new_phong_id: int=None):
        if new_ma or new_ma_serial or new_mo_ta or new_nam_su_dung or new_loai_tai_san_id or new_phong_id:
            tai_san = CRUD_TaiSan.read(tai_san_id=tai_san_id)
            if not tai_san:
                return CRUD_Status.NOT_FOUND
            if new_ma:
                tai_san.ma = new_ma
            if new_ma_serial:
                tai_san.ma_serial = new_ma_serial
            if new_mo_ta:
                tai_san.mo_ta = new_mo_ta
            if new_nam_su_dung:
                tai_san.nam_su_dung = new_nam_su_dung
            if new_loai_tai_san_id:
                tai_san.loai_tai_san_id = new_loai_tai_san_id
            if new_phong_id:
                tai_san.phong_id = new_phong_id
            return CRUD_Status.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete(tai_san_id: int):
        tai_san = CRUD_TaiSan.read(tai_san_id=tai_san_id)
        if not tai_san:
            return CRUD_Status.NOT_FOUND
        session.delete(tai_san)
        return CRUD_Status.DELETED
    
class CRUD_LichSuKiemKe:
    @staticmethod
    @crud_handler_wrapper
    def create(phong_id:int, thoi_gian:datetime=None):
        new_lich_su_kiem_ke = LichSuKiemKe(phong_id=phong_id, thoi_gian=thoi_gian)
        session.add(new_lich_su_kiem_ke)
        return CRUD_Status.CREATED

    @staticmethod
    def read(lich_su_kiem_ke_id: int):
        return session.query(LichSuKiemKe).get(lich_su_kiem_ke_id)
    
    @staticmethod
    def read_all():
        return session.query(LichSuKiemKe).all()
    
    @staticmethod
    @crud_handler_wrapper
    def update(lich_su_kiem_ke_id: int, new_phong_id:int, new_thoi_gian:datetime=None):
        if new_phong_id or new_thoi_gian:
            lich_su_kiem_ke = CRUD_LichSuKiemKe.read(lich_su_kiem_ke_id=lich_su_kiem_ke_id)
            if not lich_su_kiem_ke_id:
                return CRUD_Status.NOT_FOUND
            if new_phong_id:
                lich_su_kiem_ke.phong_id = new_phong_id
            if new_thoi_gian:
                lich_su_kiem_ke.thoi_gian = new_thoi_gian
            return CRUD_Status.UPDATED
        
    @staticmethod
    @crud_handler_wrapper
    def delete(lich_su_kiem_ke_id: int):
        lich_su_kiem_ke = CRUD_LichSuKiemKe.read(lich_su_kiem_ke_id=lich_su_kiem_ke_id)
        if not lich_su_kiem_ke:
            return CRUD_Status.NOT_FOUND
        session.delete(lich_su_kiem_ke)
        return CRUD_Status.DELETED
    
class CRUD_BanGhiKiemKe:
    @staticmethod
    @crud_handler_wrapper
    def create(lich_su_kiem_ke_id:int, trang_thai:str=None, thoi_gian:datetime=None):
        new_ban_ghi_kiem_ke = BanGhiKiemKe(lich_su_kiem_ke_id=lich_su_kiem_ke_id, trang_thai=trang_thai, thoi_gian=thoi_gian)
        session.add(new_ban_ghi_kiem_ke)
        return CRUD_Status.CREATED

    @staticmethod
    def read(ban_ghi_kiem_ke_id: int):
        return session.query(BanGhiKiemKe).get(ban_ghi_kiem_ke_id)
    
    @staticmethod
    def read_all():
        return session.query(BanGhiKiemKe).all()
    
    @staticmethod
    @crud_handler_wrapper
    def update(ban_ghi_kiem_ke_id: int, new_lich_su_kiem_ke_id:int, new_trang_thai:str=None, new_thoi_gian:datetime=None):
        if new_lich_su_kiem_ke_id or new_trang_thai or new_thoi_gian:
            ban_ghi_kiem_ke = CRUD_BanGhiKiemKe.read(ban_ghi_kiem_ke_id=ban_ghi_kiem_ke_id)
            if not ban_ghi_kiem_ke:
                return CRUD_Status.NOT_FOUND
            if new_lich_su_kiem_ke_id:
                ban_ghi_kiem_ke.lich_su_kiem_ke_id = new_lich_su_kiem_ke_id
            if new_trang_thai:
                ban_ghi_kiem_ke.trang_thai = new_trang_thai
            if new_thoi_gian:
                ban_ghi_kiem_ke.thoi_gian = new_thoi_gian
            return CRUD_Status.UPDATED
        
    @staticmethod
    @crud_handler_wrapper
    def delete(ban_ghi_kiem_ke_id: int):
        ban_ghi_kiem_ke = CRUD_BanGhiKiemKe.read(ban_ghi_kiem_ke_id=ban_ghi_kiem_ke_id)
        if not ban_ghi_kiem_ke:
            return CRUD_Status.NOT_FOUND
        session.delete(ban_ghi_kiem_ke)
        return CRUD_Status.DELETED
    
from sqlalchemy.orm import make_transient

class Handler_KiemKe:
    def __init__(self, phong_id: int) -> None:
        self.lich_su_kiem_ke = LichSuKiemKe(phong_id=phong_id)
        self.ban_ghi_kiem_kes = []

    def add(self, tai_san_id: int, trang_thai: str = None, thoi_gian: datetime = None):
        ban_ghi_kiem_ke = BanGhiKiemKe(tai_san_id=tai_san_id, trang_thai=trang_thai, thoi_gian=thoi_gian)
        self.ban_ghi_kiem_kes.append(ban_ghi_kiem_ke)

    def complete(self):
        self.lich_su_kiem_ke.thoi_gian = datetime.utcnow()
        self.lich_su_kiem_ke.ban_ghi_kiem_kes = self.ban_ghi_kiem_kes

        # Make the lich_su_kiem_ke and its associated ban_ghi_kiem_kes transient
        make_transient(self.lich_su_kiem_ke)
        for ban_ghi_kiem_ke in self.lich_su_kiem_ke.ban_ghi_kiem_kes:
            make_transient(ban_ghi_kiem_ke)

        # Add the transient objects to the session and commit
        session.add(self.lich_su_kiem_ke)
        session.commit()
