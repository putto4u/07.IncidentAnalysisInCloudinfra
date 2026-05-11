"""드로퍼(dropper) 개념을 안전하게 설명하는 교육용 코드."""
# 경로 처리를 위한 표준 라이브러리 임포트
from pathlib import Path
# JSON 출력을 보기 좋게 만들기 위한 라이브러리 임포트
import json

# 실습용 작업 폴더 경로 정의
LAB_DIR = Path("lab_dropper")
# 드롭될(생성될) 샘플 파일 경로 정의
DROPPED_FILE = LAB_DIR / "payload_sample.txt"


# 안전한 드로퍼 동작을 모사하는 함수 정의
def simulate_dropper() -> dict:
    # 작업 폴더가 없으면 생성
    LAB_DIR.mkdir(parents=True, exist_ok=True)
    # 교육용 텍스트 내용을 파일에 기록(악성 실행 파일 아님)
    DROPPED_FILE.write_text("SAFE_PAYLOAD_SAMPLE", encoding="utf-8")
    # 분석용 결과를 사전 형태로 반환
    return {
        "action": "drop_file",
        "path": str(DROPPED_FILE),
        "size": DROPPED_FILE.stat().st_size,
        "note": "execution not performed",
    }


# 스크립트 시작 지점 정의
def main() -> None:
    # 드로퍼 동작 모사 실행
    result = simulate_dropper()
    # 결과를 JSON 형태로 출력
    print(json.dumps(result, ensure_ascii=False, indent=2))


# 직접 실행 시에만 main 함수 호출
if __name__ == "__main__":
    # 메인 함수 실행
    main()
