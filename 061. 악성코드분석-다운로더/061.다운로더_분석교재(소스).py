"""다운로더 분석 강의용 무해 소스."""

# JSON 포맷 출력을 위해 json 모듈을 임포트한다.
import json
# URL 파싱을 위해 urllib.parse를 임포트한다.
from urllib.parse import urlparse

# 강의용 URL 문자열을 정의한다.
DOWNLOAD_URL = "https://example.com/sample.bin"
# 허용 도메인 목록을 정의한다.
ALLOWED_HOSTS = {"example.com"}


# URL 허용 여부를 판정하는 함수를 정의한다.
def check_allowlist(url: str) -> bool:
    # URL에서 호스트를 추출한다.
    host = urlparse(url).hostname
    # 호스트가 허용 목록에 있으면 True를 반환한다.
    return host in ALLOWED_HOSTS


# 실제 공격 동작 대신 분석 절차 설명을 반환하는 함수를 정의한다.
def simulate_download_flow() -> dict:
    # 1단계 설명 문자열을 정의한다.
    step1 = "parse URL and validate allowlist"
    # 2단계 설명 문자열을 정의한다.
    step2 = "download bytes from trusted source (placeholder only)"
    # 3단계 설명 문자열을 정의한다.
    step3 = "verify hash before any execution"
    # 핵심 공격성 코드는 제공하지 않고 설명으로 대체한다.
    return {"step1": step1, "step2": step2, "step3": step3, "offensive_code": "omitted"}


# 메인 함수를 정의한다.
def main() -> None:
    # URL 허용 여부를 계산한다.
    allowed = check_allowlist(DOWNLOAD_URL)
    # 다운로드 흐름 설명 객체를 생성한다.
    flow = simulate_download_flow()
    # 출력 결과 객체를 구성한다.
    result = {"topic": "downloader", "allowed_url": allowed, "flow": flow}
    # JSON 형태로 출력한다.
    print(json.dumps(result, ensure_ascii=False, indent=2))


# 직접 실행 시에만 main 함수를 호출한다.
if __name__ == "__main__":
    # 메인 함수를 실행한다.
    main()
