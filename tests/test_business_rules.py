from business_rules import discount_rate, gear_fee, registration_total, session_rate


def test_session_rate_beginner():
    assert session_rate("Beginner") == 45.0


def test_session_rate_intermediate():
    assert session_rate("Intermediate") == 55.0


def test_session_rate_advanced():
    assert session_rate("Advanced") == 70.0


def test_discount_rate_big_discount():
    assert discount_rate(8) == 0.15


def test_discount_rate_medium_discount():
    assert discount_rate(7) == 0.05


def test_discount_rate_small_discount():
    assert discount_rate(4) == 0.05


def test_discount_rate_no_discount():
    assert discount_rate(3) == 0.0


def test_gear_fee_below_max():
    assert gear_fee(4) == 32.0


def test_gear_fee_at_max():
    assert gear_fee(5) == 40.0


def test_gear_fee_above_max():
    assert gear_fee(6) == 40.0


def test_registration_total_beginner_no_discount_no_gear():
    assert registration_total("Beginner", 3, False, False) == 135.0


def test_registration_total_intermediate_with_discount_credit_no_gear():
    assert registration_total("Intermediate", 4, True, False) == 199.0


def test_registration_total_advanced_with_discount_credit_and_gear():
    assert registration_total("Advanced", 8, True, True) == 506.0


def test_registration_total_advanced_with_no_discount_gear():
    assert registration_total("Advanced", 2, False, True) == 156.0


def test_registration_total_beginner_with_discount_no_credit_and_no_gear():
    assert registration_total("Beginner", 4, True, False) == 171.0
