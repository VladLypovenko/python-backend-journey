import math

def validate_name(name: str) -> str:
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    return name.strip()


def validate_positive_int(value):
    if value <= 0:
        raise ValueError("Value must be greater than zero.")
    return value


def validate_non_negative_int(value):
    if value < 0:
        raise ValueError("Value cannot be negative.")
    return value


def validate_positive_float(value: float) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Value must be a finite positive number.")

    return value