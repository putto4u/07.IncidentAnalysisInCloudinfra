"""여러 행위를 종합해 탐지 점수를 계산하는 교육용 코드."""
# dataclass 사용을 위한 라이브러리 임포트
from dataclasses import dataclass


# 이벤트 구조를 정의하는 데이터클래스 선언
@dataclass
class Event:
    # 이벤트 이름 필드
    name: str
    # 이벤트 위험 점수 필드
    score: int


# 탐지 점수 계산 함수 정의
def calculate_risk(events: list[Event]) -> dict:
    # 점수 합계를 계산
    total = sum(e.score for e in events)
    # 임계값 기준으로 등급 판정
    level = "high" if total >= 10 else "medium" if total >= 5 else "low"
    # 결과 사전 반환
    return {"total_score": total, "risk_level": level}


# 메인 함수 정의
def main() -> None:
    # 샘플 이벤트 목록 생성
    events = [Event("suspicious_download", 4), Event("hash_mismatch", 4), Event("beacon_pattern", 3)]
    # 종합 위험도 계산
    result = calculate_risk(events)
    # 결과 출력
    print(result)


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 실행
    main()
