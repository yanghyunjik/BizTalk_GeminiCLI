# 업무 말투 변환기 (Biztone Converter)

이 프로젝트는 입력된 텍스트를 수신 대상(상사, 동료, 고객 등)에 맞는 적절한 비즈니스 말투로 변환해주는 웹 서비스입니다.

## 프로젝트 개요

- **목적**: 비즈니스 커뮤니케이션 고민 해결 및 업무 효율 증대
- **핵심 기술**:
    - **Backend**: Python 3.11+, FastAPI, LangChain, Upstage Solar-Pro API
    - **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
    - **AI Model**: Upstage Solar-Pro (한국어 최적화 모델)

## 시스템 아키텍처

```
[Frontend] (Vanilla JS)  <-->  [Backend] (FastAPI)  <-->  [AI] (Upstage Solar-Pro)
      index.html                  main.py                API 연동
      app.js                      convert.py
```

- **Backend 구조**:
    - `main.py`: FastAPI 앱 설정 및 CORS 미들웨어 구성
    - `routers/convert.py`: `/api/convert` 엔드포인트 처리
    - `services/tone_converter.py`: LangChain을 이용한 LLM 호출 로직
    - `prompts/templates.py`: 수신 대상별 프롬프트 템플릿
    - `models/schemas.py`: Pydantic 기반 요청/응답 데이터 스키마

## 개발 및 실행 가이드

### 1. 환경 설정

`.env` 파일을 `backend/` 디렉토리(또는 루트)에 생성하고 Upstage API 키를 설정해야 합니다.

```bash
# .env
UPSTAGE_API_KEY=your_api_key_here
```

### 2. 백엔드 실행

```bash
# 가상환경 활성화 (필요 시)
# .\venv\Scripts\activate (Windows)

# 패키지 설치
pip install -r backend/requirements.txt

# 서버 실행
cd backend
python main.py
# 또는
uvicorn main:app --reload --port 8000
```

### 3. 프론트엔드 실행

`frontend/index.html` 파일을 브라우저에서 직접 열거나, VS Code의 Live Server 확장을 사용하여 실행합니다.
기본적으로 `http://localhost:8000`의 백엔드 API를 호출하도록 설정되어 있습니다 (`frontend/js/app.js`).

## 개발 원칙 (바이브 코딩 3원칙)

프로젝트 개발 시 다음 원칙을 엄격히 준수합니다 (상세 내용은 `PRD_업무말투변환기.md` 참고).

1.  **완료 기준을 먼저 정의하라**: "끝"의 기준을 명확히 하고 불필요한 기능 확장을 지양합니다.
2.  **조사 먼저, 구현 나중**: API 연동이나 새로운 기술 도입 전 방법을 먼저 파악합니다.
3.  **버그는 분석 먼저, 수정 나중**: 에러 발생 시 원인을 먼저 분석하고 해결책을 논의합니다.

## 프로젝트 가이드라인 (AI 어시스턴트 지침)

- **언어**: 모든 응답은 한국어로 작성하며 전문 용어는 영문을 병기합니다.
- **보안**: `.env` 파일 및 API 키 노출을 절대 금지합니다.
- **Git**: `git push --force`, `git reset --hard` 등 파괴적인 명령은 지양하며 실행 전 반드시 경고합니다.
- **수정**: 파일 수정 전 영향 범위를 분석하고 사용자에게 고지합니다.
