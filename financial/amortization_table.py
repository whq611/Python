import pandas as pd

def payment(principal: float, interest_rate: float, payments: int) -> float:
    """
    Calculate the monthly payment for a loan.

    Parameters
    ----------
    principal : float
        The amount of the loan.
    interest_rate : float
        The annual interest rate for the loan.
    years : int
        The term of the loan in years.

    Returns
    -------
    float
        The monthly payment for the loan.

    Examples
    --------
    >>> payment(1000, 0.1, 1)
    1099.9999999999995
    """
    payment = principal * interest_rate / (1 - (1 + interest_rate) ** -payments)

    return payment

def amortization_table(principal: float, interest_rate: float, years: int) -> pd.DataFrame:
    """
    Create an amortization table for a loan.

    Parameters
    ----------
    principal : float
        The amount of the loan.
    interest_rate : float
        The annual interest rate for the loan.
    years : int
        The term of the loan in years.

    Returns
    -------
    pd.DataFrame
        The amortization table for the loan.

    Examples
    --------
    >>> amortization_table(1000, 0.1, 1)
        Payment  Principal  Interest  Remaining
    0      0.00       0.00      0.00    1000.00
    1     87.92      79.58      8.33     920.42
    2     87.92      80.25      7.67     840.17
    3     87.92      80.91      7.00     759.26
    4     87.92      81.59      6.33     677.67
    5     87.92      82.27      5.65     595.40
    6     87.92      82.95      4.96     512.45
    7     87.92      83.65      4.27     428.80
    8     87.92      84.34      3.57     344.46
    9     87.92      85.05      2.87     259.41
    10    87.92      85.75      2.16     173.66
    11    87.92      86.47      1.45      87.19
    12    87.92      87.19      0.73       0.00
    """
    payments = years * 12
    interest_rate /= 12
    payment_amount = payment(principal, interest_rate, payments)
    df = pd.DataFrame(index=range(0, payments + 1), columns=["Payment", "Principal", "Interest", "Remaining"], dtype="float", data=0)

    df["Payment"][1:] = payment_amount
    df["Remaining"][0] = principal
    for i in range(1, payments + 1):
        df["Interest"][i] = df["Remaining"][i - 1] * interest_rate
        df["Principal"][i] = df["Payment"][i] - df["Interest"][i]
        df["Remaining"][i] = df["Remaining"][i - 1] - df["Principal"][i]
    df = df.round(2)
    df = df.abs()

    return df



if __name__ == "__main__":
    import doctest

    doctest.testmod()