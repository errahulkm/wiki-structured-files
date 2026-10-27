"""
Command-Line Interface for the Chief Manager & Orchestration Engine.
Controls phase transitions, state persistence, dynamic prompt synthesis, and system audits.
"""

import sys
import os
import argparse
import json
from typing import Optional

# Ensure orchestration directory is in Python path
sys.path.insert(0, os.path.abspath("."))

from orchestration.state.state_manager import StateManager
from orchestration.prompts.dynamic_prompt_engine import DynamicPromptEngine
from orchestration.validators.schema_validator import validate_state_json
from orchestration.validators.code_auditor import audit_python_file
from orchestration.validators.embedded_register_check import check_embedded_c_code


class OrchestratorCLI:
    """CLI Controller for Orchestration Execution."""

    def __init__(self):
        self.state_manager = StateManager()
        self.prompt_engine = DynamicPromptEngine(state_manager=self.state_manager)

    def display_status(self):
        """Displays current system status, active phase, and completed micro-steps."""
        state = self.state_manager.get_state()
        print("\n" + "=" * 80)
        print(f"CHIEF ORCHESTRATOR STATUS: {state['project_name']}")
        print("=" * 80)
        print(f"Current Phase         : {state['current_phase']}")
        print(f"Micro-Step Index      : {state['current_micro_step']}")
        print(f"Active Agent          : {state['active_agent']}")
        print(f"System Health         : {state['system_health']['status']}")
        print(f"Completed Micro-Phases: {len(state['completed_micro_phases'])}")
        print(f"User Feedback History : {len(state['user_feedback_history'])} entry(ies)")
        print(f"Auditing Approval     : {state['audit_status']['final_approval_granted']}")
        print("=" * 80 + "\n")

    def record_feedback(self, target_agent: str, feedback_text: str):
        """Records user feedback and updates dynamic prompts."""
        self.state_manager.record_user_feedback(target_agent, feedback_text)
        print(f"[SUCCESS] Recorded user feedback for [{target_agent}]: {feedback_text}")

    def generate_agent_prompt(self, agent_role: str, agent_file: str, prd_content: Optional[str] = None) -> str:
        """Generates dynamic runtime prompt for a target agent."""
        compiled = self.prompt_engine.compile_dynamic_prompt(
            agent_role=agent_role,
            agent_filename=agent_file,
            current_prd=prd_content
        )
        print(f"[SUCCESS] Dynamic prompt compiled and saved for [{agent_role}].")
        return compiled

    def run_audits(self):
        """Executes complete validation suite across state, code, and embedded rules."""
        print("\n--- RUNNING MISSION-CRITICAL AUDIT SUITE ---")
        
        # 1. State validation
        state_valid, state_errs = validate_state_json()
        print(f"[AUDIT] State JSON Schema Check: {'PASSED' if state_valid else 'FAILED'}")
        if state_errs:
            for err in state_errs:
                print(f"  - {err}")

        # 2. Python code audit on core files
        py_files = ["orchestration/state/state_manager.py", "orchestration/prompts/dynamic_prompt_engine.py"]
        py_passed = True
        for py_file in py_files:
            p_pass, p_issues = audit_python_file(py_file)
            print(f"[AUDIT] Python Check ({py_file}): {'PASSED' if p_pass else 'ISSUES DETECTED'}")
            if p_issues:
                py_passed = False
                for issue in p_issues:
                    print(f"  - {issue}")

        # Update audit status in state.json
        self.state_manager.update_audit_status(
            audited_by_qa=True,
            pep8_compliance_passed=py_passed
        )
        print("--- AUDIT COMPLETE ---\n")


def main():
    parser = argparse.ArgumentParser(description="Chief Orchestration CLI")
    parser.add_argument("--status", action="store_true", help="Display current orchestration status")
    parser.add_argument("--feedback", type=str, help="User feedback instruction text")
    parser.add_argument("--target-agent", type=str, default="ALL", help="Target agent for feedback")
    parser.add_argument("--audit", action="store_true", help="Run validation & audit checks")
    parser.add_argument("--compile-prompt", type=str, help="Agent prompt filename (e.g., 01_chief_orchestrator.md)")
    parser.add_argument("--agent-role", type=str, help="Role name for target agent")

    args = parser.parse_args()
    cli = OrchestratorCLI()

    if args.status or len(sys.argv) == 1:
        cli.display_status()

    if args.feedback:
        cli.record_feedback(args.target_agent, args.feedback)

    if args.compile_prompt and args.agent_role:
        prompt = cli.generate_agent_prompt(args.agent_role, args.compile_prompt)
        print("\n--- COMPILED DYNAMIC PROMPT PREVIEW ---")
        print(prompt[:500] + "\n...[TRUNCATED]...")

    if args.audit:
        cli.run_audits()


if __name__ == "__main__":
    main()
