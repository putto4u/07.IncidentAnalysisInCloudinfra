"""로그 삭제/은닉 시도를 탐지 관점에서 설명하는 교육용 코드."""
# 정규표현식 매칭을 위한 라이브러리 임포트
import re


# 의심 명령 문자열 목록 정의(교육용)
SUSPICIOUS_COMMANDS = [
    "wevtutil cl System",
    "Clear-EventLog Security",
    "rm /var/log/auth.log",
]


# 흔적 제거 관련 명령 탐지 함수 정의
def detect_log_tampering(commands: list[str]) -> list[str]:
    # 탐지 결과를 담을 리스트 초기화
    detections = []
    # 삭제/클리어 관련 키워드 패턴 정의
    pattern = re.compile(r"(cl\s+\w+|clear-eventlog|rm\s+/var/log)", re.IGNORECASE)
    # 명령어를 하나씩 검사
    for cmd in commands:
        # 패턴이 발견되면 탐지 목록에 추가
        if pattern.search(cmd):
            detections.append(cmd)
    # 탐지된 명령 리스트 반환
    return detections


# 메인 함수 정의
def main() -> None:
    # 샘플 명령 목록에서 탐지 수행
    found = detect_log_tampering(SUSPICIOUS_COMMANDS)
    # 탐지 결과 출력
    print({"detections": found, "count": len(found)})


# 직접 실행 시 main 호출
if __name__ == "__main__":
    # 메인 실행
    main()
