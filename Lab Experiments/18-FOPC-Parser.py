import re

def parse_fopc(expression):
    expression = expression.strip()

    if re.fullmatch(r"[A-Za-z]+\([A-Za-z0-9_, ]+\)", expression):
        return {"type": "predicate", "value": expression}

    match = re.fullmatch(r"(forall|exists)\s+([A-Za-z])\s*:\s*(.+)", expression, re.I)
    if match:
        return {
            "type": match.group(1).lower(),
            "variable": match.group(2),
            "expression": parse_fopc(match.group(3))
        }

    if " AND " in expression.upper():
        parts = re.split(r"\s+AND\s+", expression, flags=re.I)
        return {"type": "and", "expressions": [parse_fopc(p) for p in parts]}

    if " OR " in expression.upper():
        parts = re.split(r"\s+OR\s+", expression, flags=re.I)
        return {"type": "or", "expressions": [parse_fopc(p) for p in parts]}

    return {"type": "unknown", "value": expression}

expression = "forall x: Human(x) AND Mortal(x)"
print(parse_fopc(expression))
