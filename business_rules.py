RATE = 45.0, 55.0, 70.0
MULTI_SESSION_DISCOUNT = 0.0, 0.05, 0.15
SESSION_BIG_LIMIT = 8
SESSION_SMALL_LIMIT = 4
MEMBER_CREDIT = 10.0
MEMBER_CREDIT_MIN = 200.0
GEAR_RENTAL_PER_SESSION = 8.0
GEAR_RENTAL_MAX_FEE = 40.0


def session_rate(level: str) -> float:
    """Return per session rate for that level."""
    if level == "Beginner":
        return RATE[0]
    elif level == "Intermediate":
        return RATE[1]
    else:
        return RATE[2]


def discount_rate(sessions: int) -> float:
    """Return the discount as a decimal: 0.0, 0.05, or 0.15."""
    if sessions >= SESSION_BIG_LIMIT:
        return MULTI_SESSION_DISCOUNT[2]
    elif sessions >= SESSION_SMALL_LIMIT:
        return MULTI_SESSION_DISCOUNT[1]
    else:
        return MULTI_SESSION_DISCOUNT[0]

def gear_fee(sessions: int) -> float:
    """Return the gear rental fee after the $40.00 maximum cap."""
    fee = sessions * GEAR_RENTAL_PER_SESSION
    if fee > GEAR_RENTAL_MAX_FEE:
        return GEAR_RENTAL_MAX_FEE
    else:
        return fee
    