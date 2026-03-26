# MapleStory MCP Server

## 프로젝트 개요
메이플스토리 OpenAPI를 래핑하는 MCP(Model Context Protocol) 서버. FastMCP 기반.

## 기술 스택
- Python 3.13, uv 패키지 매니저
- FastMCP (>=3.1.1), httpx (>=0.28.1)
- Nexon OpenAPI (https://open.api.nexon.com)

## 개발 명령어
- `uv run server.py` - MCP 서버 실행
- `uv sync` - 의존성 설치
- `uv add <pkg>` - 패키지 추가

## 환경 변수
- `MAPLESTORY_API_KEY` - Nexon OpenAPI 키 (필수). `.env`에 설정

## 프로젝트 구조
- `server.py` - 단일 파일 MCP 서버. 모든 tool 정의 포함
- API 카테고리: 캐릭터, 유니온, 길드, 랭킹, 히스토리, 공지

## 코드 패턴
- 모든 API 호출은 `_request()` 헬퍼를 통해 수행
- Tool 파라미터는 `Annotated[type, "설명"]` 패턴 사용
- Docstring 및 파라미터 설명은 한국어로 작성
- 캐릭터 조회 흐름: 이름 → OCID 조회 → OCID로 상세 정보 조회
