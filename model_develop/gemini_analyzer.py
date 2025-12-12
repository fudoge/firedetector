import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image

# .env 파일 로드
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 모델 초기화 (모듈 로드 시 한 번만 실행)
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    # 속도와 비용 효율적인 flash-lite 모델 사용 권장
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
else:
    model = None
    print("Warning: GOOGLE_API_KEY not found in .env file.")

def analyze_frame_with_gemini(pil_image):
    """
    PIL 이미지 객체를 받아 Gemini로 분석하고 결과를 문자열로 반환합니다.
    """
    if not model:
        return "Error: API Key is missing. Please check .env file."
    
    try:
        prompt = """
        가정집 환경의 CCTV 이미지다. 화재 위험을 분석해라.
        화재 단계를 [경고, 위험, 대피] 중 하나로 판단하고, 발화 위치와 화재 원점으로 보이는 물체, 불길 강도를 포함하여 전체 답변을 100자 이내로 핵심만 요약해라.
        화재가 감지되지 않으면 '화재 없음'이라고만 답해라.
        답변은 한국어로 작성해라.
        """
        
        # 이미지와 프롬프트를 함께 전송
        response = model.generate_content([prompt, pil_image])
        return response.text.strip()
        
    except Exception as e:
        return f"Gemini Analysis Error: {e}"
