import time
import json
import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.config import settings


logger = logging.getLogger("app")
logger.setLevel(settings.log_level)

class JsonLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)

        process_time = time.time() - start_time
        
        log_dict = {
            "url": str(request.url),
            "method": request.method,
            "status_code": response.status_code,
            "client_ip": request.client.host,
            "실행시간": f"{process_time:.4f}s",
        }
        
        logger.info(json.dumps(log_dict))
        
        return response
    