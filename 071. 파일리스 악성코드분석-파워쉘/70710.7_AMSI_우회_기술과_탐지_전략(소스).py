# This file is a harmless lab source mapped to '70710.7_AMSI_우회_기술과_탐지_전략'.
"""Defensive training source for: 70710.7_AMSI_우회_기술과_탐지_전략."""

# Import json for formatted output.
import json
# Import platform to capture runtime OS.
import platform
# Import datetime for UTC timestamp.
from datetime import datetime, timezone

# Fix the topic using the lesson file name.
TOPIC = '70710.7_AMSI_우회_기술과_탐지_전략'
# Mark this source as defensive only.
MODE = 'defensive-training'

# Build metadata for this run.
def build_metadata() -> dict:
    # Create ISO timestamp in UTC.
    now = datetime.now(timezone.utc).isoformat()
    # Collect current OS name.
    os_name = platform.system()
    # Return metadata dictionary.
    return {
        'topic': TOPIC,
        'mode': MODE,
        'timestamp': now,
        'os': os_name,
        'safety': 'no offensive behavior',
    }

# Build topic-aware checklist items.
def build_checklist() -> list[str]:
    # Define first checklist item.
    item1 = 'Detect EncodedCommand usage'
    # Define second checklist item.
    item2 = 'Review ScriptBlock logs'
    # Define third checklist item.
    item3 = 'Flag AMSI bypass patterns'
    # Return checklist list.
    return [item1, item2, item3]

# Build final result object.
def build_result() -> dict:
    # Create metadata.
    metadata = build_metadata()
    # Create checklist.
    checklist = build_checklist()
    # Return combined result.
    return {'metadata': metadata, 'checklist': checklist}

# Main execution function.
def main() -> None:
    # Build final result.
    result = build_result()
    # Print as pretty JSON.
    print(json.dumps(result, ensure_ascii=False, indent=2))

# Run main only when executed directly.
if __name__ == '__main__':
    # Execute main.
    main()
