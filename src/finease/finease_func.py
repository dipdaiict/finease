from ensure import ensure_annotations
from finease.custom_exceptions import CustomException
from finease.logger import logger
from ensure import EnsureError
from numbers import Real

@ensure_annotations
def simple_interest(principal: Real, rate: Real, time: Real) -> Real:
    """
    Calculate simple interest.

    Parameters:
        principal: The principal amount.
        rate: The annual interest rate (in percentage).
        time: The time period (in years).

    Returns:
        The simple interest.
    """
    try:
        # Validate input values
        if principal <= 0 or rate < 0 or time < 0:
            raise CustomException("Principal must be positive, and rate and time must be non-negative.")

        # Convert rate from percentage to decimal
        rate_decimal = rate / 100

        # Calculate simple interest
        interest = principal * rate_decimal * time

        return interest

    except EnsureError as error_msg:
        raise EnsureError
