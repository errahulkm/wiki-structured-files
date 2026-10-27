"""
Embedded Register & CMSIS Hardware Code Checker.
Verifies register-level precision, volatile qualifiers, and bitwise safety for STM32 targets.
"""

import re
import os
from typing import Tuple, List


def check_embedded_c_code(code_string: str) -> Tuple[bool, List[str]]:
    """Analyzes C code for bare-metal register safety compliance."""
    issues: List[str] = []

    # Check volatile qualifier usage on pointer casts if raw addresses are used
    if re.search(r'\*\(\s*(uint32_t|uint16_t|uint8_t)\s*\*\)', code_string):
        if not re.search(r'\*\(\s*volatile\s+(uint32_t|uint16_t|uint8_t)\s*\*\)', code_string):
            issues.append("Non-volatile pointer cast detected on raw memory address access. Declare as volatile.")

    # Check for CMSIS register pointer patterns (e.g. RCC->, GPIOA->, USART->)
    cmsis_patterns = [r'RCC->', r'GPIO[A-K]->', r'USART[1-8]->', r'SPI[1-6]->', r'I2C[1-4]->', r'TIM[1-9]+->']
    found_cmsis = any(re.search(pat, code_string) for pat in cmsis_patterns)
    
    if "void" in code_string and not found_cmsis and "stm32" in code_string.lower():
        issues.append("No standard CMSIS peripheral register mapping (e.g., RCC->, GPIOA->) detected in STM32 driver.")

    # Check for unbounded while loops (e.g., while(1) without break or watchdog reset)
    if re.search(r'while\s*\(\s*!\s*\([^)]+\)\s*\)\s*;', code_string):
        issues.append("Potentially blocking register bit-wait loop detected without timeout check.")

    passed = len(issues) == 0
    return passed, issues


if __name__ == "__main__":
    sample_c = """
    void USART2_Init(void) {
        RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;
        GPIOA->MODER |= (2 << 4);
    }
    """
    passed, issues = check_embedded_c_code(sample_c)
    print(f"Embedded Check Result: Passed={passed}, Issues={issues}")
