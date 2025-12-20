# Streamlit 세팅 가이드


이 문서는 streamlit 세팅 가이드를 제공합니다.

## 가상환경 및 의존성 설치
```bash
cd frontend
python3 -m venv .venv
source .venv/bin/activate # 가상환경 활성화

pip install -r requirements.txt
```

## 환경변수 설정
`.env`파일을 `frontend/`에 만들어서 아래 내용을 채우세요:
```bash
YOLO_SERVER=<YOLO_SERVER> 
YOLO_PORT=<YOLO_PORT>           # 기본 5005
FASTAPI_SERVER=<FASTAPI_SERVER> # PORT까지 입력하세요. 기본 8000
```

## 시작하기
가상환경에서는, streamlit CLI가 지원됩니다.
```bash
streamlit run app.py
```

이후, 로그에 뜨는 주소로 streamlit에 접속할 수 있습니다.