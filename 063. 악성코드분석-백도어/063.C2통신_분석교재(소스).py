"""C2 통신 패턴을 안전하게 모사하는 교육용 코드."""
# HTTP 요청 라이브러리 임포트
import requests
# 시간 정보 생성을 위한 라이브러리 임포트
from datetime import datetime, timezone

# 허용된 테스트 서버 주소 정의
BEACON_URL = "https://httpbin.org/post"


# 비콘(beacon) 데이터를 만드는 함수 정의
def build_beacon(hostname: str) -> dict:
    # UTC 기준 현재 시각을 ISO 문자열로 생성
    now = datetime.now(timezone.utc).isoformat()
    # 실제 악성 정보 대신 안전한 진단 데이터만 구성
    return {"host": hostname, "time": now, "status": "training"}


# C2 비슷한 통신을 안전하게 수행하는 함수 정의
def send_beacon(data: dict) -> dict:
    # 테스트 서버로 POST 요청 전송
    response = requests.post(BEACON_URL, json=data, timeout=10)
    # 응답 상태 코드 오류가 있으면 예외 발생
    response.raise_for_status()
    # JSON 응답 본문을 반환
    return response.json()


# 프로그램 진입 함수 정의
def main() -> None:
    # 샘플 호스트명으로 비콘 데이터 생성
    beacon = build_beacon("lab-host-01")
    # 테스트 전송 실행
    result = send_beacon(beacon)
    # 전송 확인을 위해 서버가 받은 JSON 일부 출력
    print(result.get("json", {}))


# 직접 실행 시에만 main 호출
if __name__ == "__main__":
    # 메인 함수 실행
    main()
