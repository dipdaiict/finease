import pytest
import ensure
from finease import simple_interest
from finease.custom_exceptions import CustomException
from ensure import EnsureError

simple_interest_gd_data = [
    (1000, 5, 2, 100),          # principal = 1000, rate = 5, time = 2, expected response = 100
    (2000, 7.25, 4, 580),       # principal = 2000, rate = 7.25, time = 4, expected response = 580
    (1500, 8.5, 2.5, 318.75),   # principal = 1500, rate = 8.5, time = 2.5, expected response = 318.75
    (3000, 6, 3, 540),          # principal = 3000, rate = 6, time = 3, expected response = 540
    (500, 10, 2, 100),          # principal = 500, rate = 10, time = 2, expected response = 100
    (1200, 3.75, 5, 225),       # principal = 1200, rate = 3.75, time = 5, expected response = 225
    (2500, 9, 1.5, 337.5),      # principal = 2500, rate = 9, time = 1.5, expected response = 337.5
    (800, 4.5, 4.5, 162),       # principal = 800, rate = 4.5, time = 4.5, expected response = 162
]
     
@pytest.mark.parametrize("principal, rate, time, response", simple_interest_gd_data)
def test_simple_interest(principal, rate, time, response):
    calculated_interest = round(simple_interest(principal, rate, time), 2)
    assert calculated_interest == response

simple_interest_bd_data = [
    (None, 5, 2),      # Test with None for principal
    (1000, None, 2),   # Test with None for rate
    (1000, 5, None),   # Test with None for time
    (-100, 5, 2),      # Test with negative principal
    (1000, -5, 2),     # Test with negative rate
    (1000, 5, -2),     # Test with negative time
    (0, 5, 2)        # Test with zero principal     # Test with zero rate
]

@pytest.mark.parametrize("principal, rate, time", simple_interest_bd_data)
def test_simple_interest_failed(principal, rate, time):
    with pytest.raises((CustomException, EnsureError)) as exc_info:
        simple_interest(principal, rate, time)
    assert exc_info.type in (CustomException, EnsureError)
