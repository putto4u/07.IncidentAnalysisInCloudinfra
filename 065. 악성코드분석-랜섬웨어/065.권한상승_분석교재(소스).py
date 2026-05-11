"""권한 상승 징후를 점검하는 방어 교육용 코드."""
# 현재 사용자 정보를 얻기 위한 라이브러리 임포트
import getpass
# 운영체제 정보를 얻기 위한 라이브러리 임포트
import os


# 권한 수준을 간단히 판단하는 함수 정의
def check_privilege_level() -> dict:
    # 현재 사용자 이름 조회
    user = getpass.getuser()
    # 기본 결과 구조 생성
    result = {"user": user, "is_admin_like": False, "note": "no elevation attempt"}
    # Windows에서는 관리자 그룹명 단순 확인(정확한 권한 API 아님)
    if os.name == "nt":
        result["is_admin_like"] = user.lower() in {"administrator", "admin"}
    # Unix 계열에서는 UID 0 여부로 루트 유사 판단
    else:
        result["is_admin_like"] = (os.getuid() == 0)
    # 결과 반환
    return result


# 메인 실행 함수 정의
def main() -> None:
    # 권한 수준 체크 수행
    report = check_privilege_level()
    # 결과 출력
    print(report)


# 직접 실행 조건
if __name__ == "__main__":
    # 메인 함수 실행
    main()
