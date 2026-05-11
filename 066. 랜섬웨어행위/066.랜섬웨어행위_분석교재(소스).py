"""랜섬웨어의 '파일 암호화 단계'를 안전하게 모사하는 교육용 코드."""
# Base64 인코딩을 위한 라이브러리 임포트
import base64
# 경로 처리를 위한 라이브러리 임포트
from pathlib import Path

# 샘플 원본 파일 경로 정의
SOURCE = Path("lab_ransom_source.txt")
# 모의 암호화 결과 파일 경로 정의
ENCODED = Path("lab_ransom_source.txt.encoded")


# 안전한 인코딩(암호화 모사) 함수 정의
def simulate_encryption_behavior() -> None:
    # 원본 파일이 없으면 기본 텍스트 생성
    if not SOURCE.exists():
        SOURCE.write_text("This is a safe training file.", encoding="utf-8")
    # 원본 파일을 바이트로 읽기
    raw = SOURCE.read_bytes()
    # Base64로 인코딩(복구 가능한 단순 변환)
    transformed = base64.b64encode(raw)
    # 결과 파일로 저장
    ENCODED.write_bytes(transformed)


# 메인 함수 정의
def main() -> None:
    # 모의 암호화 행위 실행
    simulate_encryption_behavior()
    # 완료 메시지 출력
    print(f"created: {ENCODED}")


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 함수 호출
    main()
