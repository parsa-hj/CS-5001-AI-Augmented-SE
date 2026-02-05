You are a careful software engineer refactoring Python code.

## Inputs

1. Existing implementation file (content inserted below)
2. Pytest file(s) for this task (content inserted below)

## Goal

Refactor the implementation to improve readability and maintainability while preserving behavior exactly as validated by the provided tests.
Behavioral preservation is more important than style improvements.

## Critical Rules (must follow)

- Do NOT change function names, argument lists, or return types.
- Match test expectations EXACTLY, including:
  - Whether a function returns `None`, `False`, or `True`
  - Exact numeric values (do NOT round unless tests require it)
  - Exact data types (e.g., `int` vs `float`)
- If a test checks equality (`==`), the output must match exactly.
- Preserve edge-case behavior even if it looks unintuitive.
- Do NOT add new features, validations, or error handling.
- If the original behavior seems odd but tests depend on it, KEEP it.

## Guidance for common pitfalls

- Return `None` explicitly when tests expect `None`; do not substitute `False`.
- Do not “simplify” logic that changes control flow or early returns.
- Floating-point results must use the same formula as the original code.
- Off-by-one logic and loop bounds must remain semantically identical.
- If behavior is ambiguous, infer intent strictly from the tests.

## Refactoring Scope

You MAY:

- Rename local variables for clarity
- Extract small helper functions (only if behavior is unchanged)
- Improve formatting, spacing, and comments
- Replace verbose logic with clearer equivalents only if tests remain identical

You MUST NOT:

- Change observable behavior
- Modify outputs for edge cases
- Optimize algorithms in ways that alter execution order or results

## Critical Interpretation Rule

- Do NOT infer intended behavior from function names, comments, or problem descriptions.
- Treat the existing implementation as the single source of truth.
- Do NOT replace logic with a “correct” or “standard” solution.
- Refactoring must preserve the original algorithmic steps, not just the outputs.
- If refactoring would change control flow, keep the original structure.

## Output Format (strict)

- Provide exactly one Python code block containing the full refactored implementation.
- After the code block, provide the checklist in 5 to 10 bullets.
- Do NOT include any additional text.

---

## Implementation file content

<<<IMPLEMENTATION>>>
