"""지속성(persistence) 기법을 '등록 시도 없이' 설명하는 교육용 코드."""
# JSON 출력 포맷용 라이브러리 임포트
import json
# 플랫폼 정보를 확인하기 위한 라이브러리 임포트
import platform


# 지속성 후보 위치를 학습용으로 보여주는 함수 정의
def list_persistence_locations() -> dict:
    # 현재 운영체제 이름 수집
    os_name = platform.system().lower()
    # 운영체제별 대표 지속성 위치를 텍스트로 정의(실제 수정 없음)
    if "windows" in os_name:
        locations = ["HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "작업 스케줄러"]
    else:
        locations = ["~/.config/autostart", "crontab -e"]
    # 분석 결과를 반환
    return {"os": os_name, "possible_locations": locations, "action": "read-only guidance"}


# 메인 함수 정의
def main() -> None:
    # 지속성 위치 목록 수집
    result = list_persistence_locations()
    # 사람이 읽기 쉬운 JSON으로 출력
    print(json.dumps(result, ensure_ascii=False, indent=2))


# 파일 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 함수 호출
    main()
