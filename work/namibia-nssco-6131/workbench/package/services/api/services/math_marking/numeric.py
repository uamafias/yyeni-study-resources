"""Pure finite-number parsing used by frozen marking-contract validation."""
from decimal import Decimal, InvalidOperation


def finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        return None
    try:
        number = Decimal(str(value).strip())
    except (InvalidOperation, ValueError, TypeError):
        return None
    return number if number.is_finite() else None
