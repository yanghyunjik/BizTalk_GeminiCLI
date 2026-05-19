import sys
import os

# Vercel 서버리스 환경에서 모듈 임포트 경로 설정
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import convert
from mangum import Mangum

app = FastAPI(title="업무 말투 변환기 API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(convert.router, prefix="/api")

# Health Check - /health 와 /api/health 둘 다 대응 (임시: 환경 변수 확인용)
@app.get("/health")
@app.get("/api/health")
async def health_check():
    key = os.environ.get("UPSTAGE_API_KEY", "")
    return {
        "status": "ok",
        "upstage_key_set": bool(key),
        "key_preview": (key[:6] + "...") if key else "NOT SET"
    }

# 로컬 개발 환경에서만 정적 파일 서빙 (Vercel은 routes로 직접 처리)
if not os.environ.get("VERCEL"):
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
    css_path = os.path.join(frontend_path, "css")
    js_path = os.path.join(frontend_path, "js")
    if os.path.exists(css_path):
        app.mount("/css", StaticFiles(directory=css_path), name="css")
    if os.path.exists(js_path):
        app.mount("/js", StaticFiles(directory=js_path), name="js")

    @app.get("/")
    async def read_index():
        return FileResponse(os.path.join(frontend_path, "index.html"))

# Vercel 서버리스 함수 핸들러
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
