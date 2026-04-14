# 030. 자동화-효율적리소스 운영 - 03. 작업 자동화 기반의 인시던트 대응 (SOAR)

## 개요
보안 운영 자동화 및 오케스트레이션 및 대응(SOAR)은 클라우드 환경에서 발생하는 인시던트에 대해 신속하고 효율적으로 대응하기 위한 핵심 전략입니다. Event-Driven remediation, 자동화된 워크플로우 설계, 그리고 Self-Healing 인프라는 SOAR의 주요 구성 요소입니다.

## 3.1 Event-Driven Remediation: AWS Lambda 및 EventBridge를 활용한 비정상 리소스 즉시 격리 아키텍처
클라우드 환경에서는 이벤트 기반(Event-Driven) 아키텍처를 활용하여 보안 위협에 대한 자동화된 대응이 가능합니다. AWS Lambda 및 EventBridge는 이러한 Event-Driven remediation을 구현하기 위한 강력한 도구입니다.
- **AWS EventBridge:** 다양한 AWS 서비스 및 SaaS 애플리케이션에서 발생하는 이벤트를 중앙 집중식으로 라우팅하고, 특정 규칙에 따라 대상 서비스(예: AWS Lambda)로 전달합니다.
- **AWS Lambda:** 이벤트에 의해 트리거되는 서버리스 함수를 실행하여, 비정상적인 리소스에 대한 즉각적인 격리 또는 수정 작업을 수행합니다.
- **비정상 리소스 즉시 격리 시나리오:**
    1. 비정상적인 IAM 활동이 CloudTrail에 기록됩니다.
    2. CloudTrail 로그 이벤트가 EventBridge 규칙에 의해 감지됩니다.
    3. EventBridge는 AWS Lambda 함수를 트리거합니다.
    4. Lambda 함수는 해당 IAM 사용자의 권한을 즉시 무효화하거나, 관련 리소스를 격리합니다.

## 3.2 자동화된 워크플로우 설계: n8n 또는 Tines를 활용하여 API 기반의 보안 장비 연동 및 차단 자동화
SOAR 플랫폼은 다양한 보안 솔루션 및 장비들을 통합하여 복잡한 보안 워크플로우를 자동화하는 역할을 합니다. n8n 또는 Tines와 같은 도구는 API 기반으로 이러한 통합 및 자동화를 가능하게 합니다.
- **n8n / Tines의 역할:**
    - **통합:** SIEM, EDR, 방화벽, 위협 인텔리전스 플랫폼 등 다양한 보안 솔루션과 API를 통해 연동합니다.
    - **워크플로우 시각화:** 복잡한 인시던트 대응 프로세스를 시각적인 워크플로우 형태로 설계하고 자동화합니다.
    - **자동화된 대응:** 특정 보안 이벤트 발생 시, 자동으로 관련 정보를 수집하고, 방화벽 차단, 계정 잠금, 티켓 생성 등의 대응 작업을 수행합니다.
- **API 기반 연동:** 각 보안 장비의 API를 활용하여 데이터를 주고받고, 명령을 실행함으로써 수동 작업을 최소화하고 대응 시간을 단축합니다.

## 3.3 Self-Healing 인프라: 테라폼(Terraform) 및 OpenTofu를 이용한 드리프트(Drift) 탐지 및 자동 복구
Self-Healing 인프라는 인프라의 설정이 의도하지 않게 변경(드리프트)되었을 때, 이를 탐지하고 자동으로 원래 상태로 복구하는 개념입니다. Terraform 및 OpenTofu와 같은 IaC(Infrastructure as Code) 도구는 이를 구현하는 데 핵심적인 역할을 합니다.
- **드리프트(Drift) 탐지:** IaC 코드로 정의된 인프라의 기준 상태와 실제 운영 중인 인프라의 상태를 비교하여 불일치를 감지합니다.
- **자동 복구 메커니즘:**
    1. 드리프트 탐지 시스템이 변경 사항을 감지합니다.
    2. 자동화된 워크플로우가 트리거됩니다.
    3. Terraform 또는 OpenTofu를 사용하여 인프라를 코드에 정의된 상태로 재적용(apply)하여 드리프트를 복구합니다.
- **보안 측면의 이점:** 악의적인 변경이나 설정 오류로 인한 보안 취약점을 자동으로 수정하여 인프라의 보안 상태를 지속적으로 유지합니다.

## 핵심 요약
SOAR는 Event-Driven remediation, 자동화된 워크플로우 설계, 그리고 Self-Healing 인프라를 통해 클라우드 인시던트 대응의 효율성과 신속성을 극대화합니다. AWS Lambda/EventBridge, SOAR 플랫폼(n8n/Tines), 그리고 IaC 도구(Terraform/OpenTofu)의 통합은 이러한 자동화된 대응 체계를 구축하는 데 필수적입니다.

## 참고 자료
- AWS EventBridge 공식 문서: [https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-eventbridge.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-eventbridge.html)
- AWS Lambda 공식 문서: [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/)
- n8n 공식 GitHub: [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)
- OpenTofu 공식 문서: [https://opentofu.org/docs/](https://opentofu.org/docs/)