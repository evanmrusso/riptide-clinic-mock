from business_rules import session_rate, discount_rate, gear_fee

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
    
    

    