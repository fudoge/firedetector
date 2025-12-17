import logging

from firebase_admin import credentials, messaging

from src.core.config import settings
from src.db.models.fcm_data import FCMData

logger = logging.getLogger("app")
logger.setLevel(settings.log_level)

registration_token = settings.registration_token


class FCMService:
    """
    FCMService - 주요 FCM 비즈니스 로직 레이어
    """

    def __init__(self, fcm_repo):
        self.fcm_repo = fcm_repo

    def register_client(self, id, token):
        try:
            self.fcm_repo.register(id, token)
        except Exception as e:
            raise e

    def notify_client(self):
        try:
            # 모든 토큰 클라이언트들 가져오기
            fcm_datas = self.fcm_repo.getall()
            # See documentation on defining a message payload.
            message = messaging.Message(
                data={
                    "title": "화재 감지 발생!",
                    "body": "화재가 감지되었습니다",
                },
                token=registration_token,
            )
            response = messaging.send(message)
        except Exception as e:
            raise e
