"""프로세스 인젝션 개념을 '실행 없이' 흐름도로 설명하는 코드."""
# 보기 좋은 출력용 라이브러리 임포트
import json


# 인젝션 개념 단계를 텍스트로 정리하는 함수 정의
def describe_injection_steps() -> list[dict]:
    # 실제 메모리 조작 대신 설명 단계만 반환
    return [
        {"step": 1, "name": "target_process_select", "risk": "high"},
        {"step": 2, "name": "memory_write_attempt", "risk": "high"},
        {"step": 3, "name": "remote_thread_create", "risk": "high"},
        {"step": 4, "name": "execution", "risk": "critical"},
    ]


# 메인 함수 정의
def main() -> None:
    # 개념 단계 리스트 생성
    steps = describe_injection_steps()
    # JSON으로 출력
    print(json.dumps({"technique": "process_injection", "steps": steps}, ensure_ascii=False, indent=2))


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 호출
    main()
