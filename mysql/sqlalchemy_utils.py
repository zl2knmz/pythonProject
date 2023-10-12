from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mysql.db_model import User

engine = create_engine("mysql+pymysql://root:123456@192.168.16.231:3306/accupasscn?charset=utf8", max_overflow=5)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    with get_session() as session:
        ret = session.query(User).first()
        print(ret.id, ret.name, ret.password, ret.status, ret.create_date)

        str = "123"+"fdaf"
        print(str)

        # obj = User(name="alex", password='sb123', status=1, create_date='2023-09-11 00:00:00')
        # session.add(obj)
        # session.commit()
