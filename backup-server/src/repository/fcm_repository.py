from sqlalchemy.orm import Session

from src.db.models.fcm_data import FCMData


class FCMRepository:
    """
    fcm_data 테이블에 대한 데이터베이스 액세스 영역
    """

    def __init__(self, db: Session):
        self.db = db

    def register(self, token):
        new_device = FCMData(token=token)
        self.db.add(new_device)
        self.db.commit()

    def getall(self):
        fcm_datas = self.db.query(FCMData).all()
        return fcm_datas
