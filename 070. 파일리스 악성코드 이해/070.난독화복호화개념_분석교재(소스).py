"""난독화/복호화 개념을 안전 문자열로 설명하는 교육용 코드."""
# Base64 변환 라이브러리 임포트
import base64


# 문자열 난독화(인코딩) 함수 정의
def obfuscate(text: str) -> str:
    # UTF-8 바이트로 변환 후 Base64 문자열로 반환
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


# 문자열 복호화(디코딩) 함수 정의
def deobfuscate(obf: str) -> str:
    # Base64 문자열을 원문 UTF-8 문자열로 복원
    return base64.b64decode(obf.encode("ascii")).decode("utf-8")


# 메인 함수 정의
def main() -> None:
    # 원본 샘플 문자열 정의
    original = "training_command"
    # 난독화 결과 생성
    obf = obfuscate(original)
    # 복호화 결과 생성
    restored = deobfuscate(obf)
    # 결과 출력
    print({"original": original, "obfuscated": obf, "restored": restored})


# 직접 실행 시 main 호출
if __name__ == "__main__":
    # 메인 실행
    main()
