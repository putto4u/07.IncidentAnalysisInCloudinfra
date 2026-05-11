"""네트워크 스캔 개념을 안전하게 재현하는 교육용 코드."""
# 소켓 연결 테스트용 라이브러리 임포트
import socket

# 교육용 대상 호스트 정의(로컬호스트)
TARGET_HOST = "127.0.0.1"
# 교육용 대상 포트 목록 정의
TARGET_PORTS = [22, 80, 443]


# 포트 열림 여부를 확인하는 함수 정의
def check_port(host: str, port: int, timeout: float = 0.3) -> bool:
    # TCP 소켓 생성
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 타임아웃 설정
        sock.settimeout(timeout)
        # 연결 시도 결과 코드 확인(0이면 성공)
        return sock.connect_ex((host, port)) == 0


# 메인 함수 정의
def main() -> None:
    # 결과를 담을 리스트 초기화
    results = []
    # 포트를 하나씩 확인
    for port in TARGET_PORTS:
        # 열림 여부 확인 결과 저장
        results.append({"host": TARGET_HOST, "port": port, "open": check_port(TARGET_HOST, port)})
    # 최종 결과 출력
    print(results)


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 호출
    main()
