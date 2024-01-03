from enum import Enum
from typing import Callable, List, Tuple
from Backend.Database.db_models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an SQLite engine
# echo = True to logging any SQL query to console
engine = create_engine("sqlite:///Backend/Database/db.sqlite", echo=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
# default_session = Session()

session = Session()

class CRUDStatus(Enum):
    NOT_FOUND = 'Not Found'
    CREATED = 'Created'
    UPDATED = 'Updated'
    DELETED = 'Deleted'
    FAIL = 'Fail'

def crud_handler_wrapper(func: Callable)->Callable:
    def wrapper(*args, **kwargs)->Tuple[CRUDStatus, any]:
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            return CRUDStatus.FAIL

    return wrapper

class KhuCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_khu(ten: str):
        new_khu = Khu(ten=ten)
        session.add(new_khu)
        return CRUDStatus.CREATED

    @staticmethod
    def read_khu(khu_id: int):
        return session.query(Khu).get(khu_id)
    
    @staticmethod
    def read_all_khu():
        return session.query(Khu).all()

    @staticmethod
    @crud_handler_wrapper
    def update_khu(khu_id: int, new_ten: str=None):
        if new_ten:
            khu = KhuCRUD.read_khu(khu_id=khu_id)
            if not khu:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                khu.ten = new_ten
            return CRUDStatus.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete_khu(khu_id: int):
        khu = KhuCRUD.read_khu(khu_id=khu_id)
        if not khu:
            return CRUDStatus.NOT_FOUND
        session.delete(khu)
        return CRUDStatus.DELETED


class CanBoCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_can_bo(ten: str, sdt: str=None):
        new_can_bo = CanBo(ten=ten, sdt=sdt)
        session.add(new_can_bo)
        return CRUDStatus.CREATED

    @staticmethod
    def read_can_bo(can_bo_id: int):
        return session.query(CanBo).get(can_bo_id)
    
    @staticmethod
    def read_all_can_bo():
        return session.query(CanBo).all()

    @staticmethod
    @crud_handler_wrapper
    def update_can_bo(can_bo_id: int, new_ten: str=None, new_sdt: str=None):
        if new_ten or new_sdt:
            can_bo = CanBoCRUD.read_can_bo(can_bo_id=can_bo_id)
            if not can_bo:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                can_bo.ten = new_ten
            if new_sdt:
                can_bo.sdt = new_sdt
            return CRUDStatus.UPDATED

    @staticmethod
    def delete_can_bo(can_bo_id: int):
        can_bo = CanBoCRUD.read_can_bo(can_bo_id=can_bo_id)
        if not can_bo:
            return CRUDStatus.NOT_FOUND
        session.delete(can_bo)
        return CRUDStatus.DELETED

class DonViCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_don_vi(ten: str):
        new_don_vi = DonVi(ten=ten)
        session.add(new_don_vi)
        return CRUDStatus.CREATED

    @staticmethod
    def read_don_vi(don_vi_id: int):
        return session.query(DonVi).get(don_vi_id)
    
    @staticmethod
    def read_all_don_vi():
        return session.query(DonVi).all()

    @staticmethod
    def update_don_vi(don_vi_id: int, new_ten: str=None):
        if new_ten:
            don_vi = DonViCRUD.read_don_vi(don_vi_id=don_vi_id)
            if not don_vi:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                don_vi.ten = new_ten
            return CRUDStatus.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete_don_vi(don_vi_id: int):
        don_vi = DonViCRUD.read_don_vi(don_vi_id=don_vi_id)
        if not don_vi:
            return CRUDStatus.NOT_FOUND
        session.delete(don_vi)
        return CRUDStatus.DELETED


class PhongCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_phong(ten: str, thong_tin: str=None, khu_id: int=None, don_vi_id: int=None, can_bo_id: int=None):
        new_phong = Phong(ten=ten, thong_tin=thong_tin, khu_id=khu_id, don_vi_id=don_vi_id, can_bo_id=can_bo_id)
        session.add(new_phong)
        return CRUDStatus.CREATED

    @staticmethod
    def read_phong(phong_id: int):
        return session.query(Phong).get(phong_id)
    
    @staticmethod
    def read_all_phong():
        return session.query(Phong).all()

    @staticmethod
    @crud_handler_wrapper
    def update_phong(phong_id: int, new_ten: str=None, new_thong_tin: str=None, new_khu_id: int=None, new_don_vi_id: int=None, new_can_bo_id: int=None):
        if new_ten or new_can_bo_id or new_don_vi_id or new_khu_id or new_thong_tin:
            phong = PhongCRUD.read_phong(phong_id=phong_id)
            if not phong:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                phong.ten = new_ten
            if new_thong_tin:
                phong.thong_tin = new_thong_tin
            if new_khu_id:
                phong.khu_id = new_khu_id
            if new_don_vi_id:
                phong.don_vi_id = new_don_vi_id
            if new_can_bo_id:
                phong.can_bo_id = new_can_bo_id
            return CRUDStatus.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete_phong(phong_id: int):
        phong = PhongCRUD.read_phong(phong_id=phong_id)
        if not phong:
            return CRUDStatus.NOT_FOUND
        session.delete(phong)
        return CRUDStatus.DELETED


class NhomTaiSanCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_nhom_tai_san(ten: str):
        new_nhom_tai_san = NhomTaiSan(ten=ten)
        session.add(new_nhom_tai_san)
        return CRUDStatus.CREATED

    @staticmethod
    def read_nhom_tai_san(nhom_tai_san_id: int):
        return session.query(NhomTaiSan).get(nhom_tai_san_id)
    
    @staticmethod
    def read_all_nhom_tai_san():
        return session.query(NhomTaiSan).all()

    @staticmethod
    @crud_handler_wrapper
    def update_nhom_tai_san(nhom_tai_san_id: int, new_ten: str=None):
        if new_ten:
            nhom_tai_san = NhomTaiSanCRUD.read_nhom_tai_san(nhom_tai_san_id=nhom_tai_san_id)
            if not nhom_tai_san:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                nhom_tai_san.ten = new_ten
            return CRUDStatus.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete_nhom_tai_san(nhom_tai_san_id: int):
        nhom_tai_san = NhomTaiSanCRUD.read_nhom_tai_san(nhom_tai_san_id=nhom_tai_san_id)
        if not nhom_tai_san:
            return CRUDStatus.NOT_FOUND
        session.delete(nhom_tai_san)
        return CRUDStatus.DELETED


class TaiSanCRUD:
    @staticmethod
    @crud_handler_wrapper
    def create_tai_san(ten: str, ma_phan_loai: str=None, ma_dinh_danh: str=None, ma_serial: str=None, mo_ta: str=None, nam_su_dung: str=None, nhom_tai_san_id: int=None, phong_id: int=None):
        new_tai_san = TaiSan(ten=ten, ma_phan_loai=ma_phan_loai, ma_dinh_danh=ma_dinh_danh, ma_serial=ma_serial, mo_ta=mo_ta, nam_su_dung=nam_su_dung, nhom_tai_san_id=nhom_tai_san_id, phong_id=phong_id)
        session.add(new_tai_san)
        return CRUDStatus.CREATED

    @staticmethod
    def read_tai_san(tai_san_id: int):
        return session.query(TaiSan).get(tai_san_id)
    
    @staticmethod
    def read_all_tai_san():
        return session.query(TaiSan).all()

    @staticmethod
    @crud_handler_wrapper
    def update_tai_san(tai_san_id: int, new_ten: str, new_ma_phan_loai: str, new_ma_dinh_danh: str, new_ma_serial: str, new_mo_ta: str, new_nam_su_dung: str, new_nhom_tai_san_id: int, new_phong_id: int):
        if new_ten or new_ma_phan_loai or new_ma_dinh_danh or new_ma_serial or new_mo_ta or new_nam_su_dung or new_nhom_tai_san_id or new_phong_id:
            tai_san = TaiSanCRUD.read_tai_san(tai_san_id=tai_san_id)
            if not tai_san:
                return CRUDStatus.NOT_FOUND
            if new_ten:
                tai_san.ten = new_ten
            if new_ma_phan_loai:
                tai_san.ma_phan_loai = new_ma_phan_loai
            if new_ma_dinh_danh:
                tai_san.ma_dinh_danh = new_ma_dinh_danh
            if new_ma_serial:
                tai_san.ma_serial = new_ma_serial
            if new_mo_ta:
                tai_san.mo_ta = new_mo_ta
            if new_nam_su_dung:
                tai_san.nam_su_dung = new_nam_su_dung
            if new_nhom_tai_san_id:
                tai_san.nhom_tai_san_id = new_nhom_tai_san_id
            if new_phong_id:
                tai_san.phong_id = new_phong_id
            return CRUDStatus.UPDATED

    @staticmethod
    @crud_handler_wrapper
    def delete_tai_san(tai_san_id: int):
        tai_san = TaiSanCRUD.read_tai_san(tai_san_id=tai_san_id)
        if not tai_san:
            return CRUDStatus.NOT_FOUND
        session.delete(tai_san)
        return CRUDStatus.DELETED