"""키로깅 개념을 안전하게 설명하기 위한 교육용 코드."""
# 시간 대기 함수를 쓰기 위한 라이브러리 임포트
import time


# 키 입력 대신 미리 정의된 샘플 이벤트를 반환하는 함수 정의
def simulate_key_events() -> list[str]:
    # 실제 사용자 입력을 훔치지 않고 고정 문자열만 사용
    return ["K", "E", "Y", "_", "L", "A", "B"]


# 이벤트를 화면에 출력하는 함수 정의
def print_events(events: list[str]) -> None:
    # 이벤트를 하나씩 순회
    for key in events:
        # 교육용으로 키 이벤트 출력
        print(f"event={key}")
        # 로그 흐름을 보기 좋게 0.1초 대기
        time.sleep(0.1)


# 메인 함수 정의
def main() -> None:
    # 샘플 키 이벤트 생성
    events = simulate_key_events()
    # 이벤트 출력
    print_events(events)


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 호출
    main()
