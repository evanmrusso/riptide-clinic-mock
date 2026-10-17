from business_rules import session_rate, discount_rate 

def test_session_rate():
    assert session_rate("Beginner") == 45.0
    assert session_rate("Intermediate") == 55.0
    assert session_rate("Advanced") == 70.0

def test_discount_rate():
    assert discount_rate(3) == 0.0
    assert discount_rate(4) == 0.05
    assert discount_rate(7) == 0.05
    assert discount_rate(8) == 0.15