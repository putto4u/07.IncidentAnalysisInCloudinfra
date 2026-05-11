"""스크립트 로더 개념을 안전하게 모사하는 교육용 코드."""
# 문자열 템플릿 처리를 위한 라이브러리 임포트
from string import Template


# 원격에서 가져온 스크립트를 가정한 템플릿(실행하지 않음)
SAFE_SCRIPT_TEMPLATE = Template("print('hello from $env')")


# 템플릿 채우기 함수 정의
def build_script(env_name: str) -> str:
    # 주어진 환경 이름으로 템플릿 변수 치환
    return SAFE_SCRIPT_TEMPLATE.substitute(env=env_name)


# 메인 함수 정의
def main() -> None:
    # 샘플 스크립트 텍스트 생성
    script_text = build_script("training")
    # 생성된 스크립트를 출력만 수행(실행 금지)
    print(script_text)


# 직접 실행 시 동작
if __name__ == "__main__":
    # 메인 실행
    main()
