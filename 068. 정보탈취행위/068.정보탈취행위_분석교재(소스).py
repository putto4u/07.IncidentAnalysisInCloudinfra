"""정보 탈취(exfiltration) 흐름을 안전 데이터로 모사하는 코드."""
# JSON 직렬화를 위한 라이브러리 임포트
import json
# SHA-256 요약값 계산용 라이브러리 임포트
import hashlib


# 민감정보 대신 안전 샘플 데이터를 준비하는 함수 정의
def collect_safe_data() -> dict:
    # 테스트 데이터 반환
    return {"project": "incident-lab", "version": "1.0", "type": "non-sensitive"}


# 전송 전 축약 요약값을 생성하는 함수 정의
def summarize_payload(data: dict) -> str:
    # dict를 문자열로 바꾼 뒤 바이트 인코딩
    raw = json.dumps(data, sort_keys=True).encode("utf-8")
    # SHA-256 해시 계산 결과 반환
    return hashlib.sha256(raw).hexdigest()


# 메인 함수 정의
def main() -> None:
    # 샘플 데이터 수집
    payload = collect_safe_data()
    # 요약 해시 계산
    digest = summarize_payload(payload)
    # 결과 출력
    print({"payload": payload, "digest": digest})


# 직접 실행 시에만 main 호출
if __name__ == "__main__":
    # 메인 실행
    main()
