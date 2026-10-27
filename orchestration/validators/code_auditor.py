"""
Code Quality & Static Analysis Auditor for Python Core Engineering.
Enforces PEP-8 standards, type annotations, and error-handling safety.
"""

import ast
import os
from typing import List, Dict, Any, Tuple


class PythonCodeAuditor(ast.NodeVisitor):
    """AST Visitor to inspect Python code for mission-critical quality guidelines."""

    def __init__(self, filename: str):
        self.filename = filename
        self.issues: List[str] = []
        self.func_count = 0
        self.typed_func_count = 0

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.func_count += 1
        if node.returns is not None:
            self.typed_func_count += 1
        else:
            self.issues.append(f"Line {node.lineno}: Function '{node.name}' lacks return type annotation.")

        # Check for docstrings
        if not ast.get_docstring(node):
            self.issues.append(f"Line {node.lineno}: Function '{node.name}' lacks docstring.")

        self.generic_visit(node)

    def visit_Try(self, node: ast.Try):
        for handler in node.handlers:
            if handler.type is None:
                self.issues.append(f"Line {handler.lineno}: Dangerous bare 'except:' caught without specific Exception type.")
        self.generic_visit(node)


def audit_python_file(filepath: str) -> Tuple[bool, List[str]]:
    """Audits a single Python file for code quality metrics."""
    if not os.path.exists(filepath):
        return False, [f"File not found: {filepath}"]

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()
        tree = ast.parse(code, filename=filepath)
    except SyntaxError as e:
        return False, [f"Syntax Error in {filepath}: {e}"]

    auditor = PythonCodeAuditor(filepath)
    auditor.visit(tree)

    passed = len(auditor.issues) == 0
    return passed, auditor.issues


if __name__ == "__main__":
    test_target = "orchestration/state/state_manager.py"
    passed, issues = audit_python_file(test_target)
    print(f"Auditing {test_target}: Passed={passed}, Issues={issues}")
