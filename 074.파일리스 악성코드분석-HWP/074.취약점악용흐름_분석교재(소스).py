"""취약점 악용 흐름을 실제 공격 없이 단계적으로 설명하는 코드."""
# JSON 출력 포맷용 라이브러리 임포트
import json


# 공격 체인을 교육용 단계로 정의하는 함수
def build_attack_chain() -> list[dict]:
    # 각 단계는 설명 목적이며 실제 페이로드/익스플로잇 없음
    return [
        {"phase": "recon", "description": "surface identification"},
        {"phase": "weaponization", "description": "payload preparation (simulated)"},
        {"phase": "delivery", "description": "transport vector selection"},
        {"phase": "exploitation", "description": "vulnerability trigger (concept only)"},
        {"phase": "installation", "description": "persistence attempt (concept only)"},
    ]


# 메인 함수 정의
def main() -> None:
    # 단계 데이터 생성
    chain = build_attack_chain()
    # 보기 좋게 JSON 출력
    print(json.dumps({"topic": "exploit-lifecycle", "chain": chain}, ensure_ascii=False, indent=2))


# 직접 실행 시 main 호출
if __name__ == "__main__":
    # 메인 실행
    main()
