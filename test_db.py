from Backend.Database.db_models import *
from Backend.Database.db_sessions import Session

if __name__ == "__main__":
    session = Session()

    khu_a = Khu(ten="Khu A")
    don_vi_x = DonVi(ten="X")

    # Create a Phong instance
    phong_1 = Phong(ten="Phong 1")
    phong_2 = Phong(ten="Phong 2")

    # Establish the relationship
    phong_1.khu = khu_a
    phong_1.don_vi = don_vi_x
    phong_2.khu = khu_a

    # Add instances to the session
    session.add(khu_a)
    session.add(phong_1)
    session.add(phong_2)

    # Commit the changes
    session.commit()
    