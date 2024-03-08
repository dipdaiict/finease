## Usage

To use Finease, you can import it into your Python scripts or interactive sessions:

```python
from finease import simple_interest

# Calculate simple interest
principal = 1000
rate = 5
time = 2
interest = simple_interest(principal, rate, time)
print("Simple interest:", interest)
```

This will output:

```
Simple interest: 100.0
```

Args:
`simple_interest` function takes three arguments:
- `principal`: The principal amount (float or int).
- `rate`: The annual interest rate (float or int).
- `time`: The time period in years (float or int).

Retruns:
- result: result is float.
```