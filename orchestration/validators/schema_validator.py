"""
Schema Validator for Orchestration State JSON.
Verifies structural compliance of state.json against state_schema.json.
"""

import json
import os
from typing import Tuple, List, Dict, Any


def validate_state_json(state_file: str = "orchestration/state/state.json",
                        schema_file: str = "orchestration/config/state_schema.json") -> Tuple[bool, List[str]]:
    """
    Validates state_file against schema_file.
    Returns (is_valid, list_of_errors).
    """
    errors: List[str] = []

    if not os.path.exists(state_file):
        return False, [f"State file missing at: {state_file}"]

    if not os.path.exists(schema_file):
        return False, [f"Schema file missing at: {schema_file}"]

    try:
        with open(state_file, "r", encoding="utf-8") as f:
            state_data = json.load(f)
    except json.JSONDecodeError as err:
        return False, [f"JSON Syntax Error in state file: {err}"]

    try:
        with open(schema_file, "r", encoding="utf-8") as f:
            schema_data = json.load(f)
    except json.JSONDecodeError as err:
        return False, [f"JSON Syntax Error in schema file: {err}"]

    # Basic structural field validation
    required_fields = schema_data.get("required", [])
    for field in required_fields:
        if field not in state_data:
            errors.append(f"Missing required field: '{field}' in state.json")

    # Check nested audit status structure if present
    if "audit_status" in state_data:
        audit = state_data["audit_status"]
        if not isinstance(audit, dict):
            errors.append("'audit_status' must be an object")
        elif "final_approval_granted" not in audit:
            errors.append("Missing 'final_approval_granted' in 'audit_status'")

    is_valid = len(errors) == 0
    return is_valid, errors


if __name__ == "__main__":
    valid, errs = validate_state_json()
    if valid:
        print("[SUCCESS] state.json passed schema validation.")
    else:
        print(f"[FAIL] state.json validation failed: {errs}")
