def calculate_dividend_yield(dividend_per_share, market_price_per_share):
    """
    Calculate dividend yield.

    Parameters:
    - dividend_per_share (float): Annual dividend per share.
    - market_price_per_share (float): Current market price per share.

    Returns:
    - float: Dividend yield.
    """
    dividend_yield = (dividend_per_share / market_price_per_share) * 100
    return dividend_yield

# Example usage:
dividend = float(input("Enter the annual dividend per share: "))
market_price = float(input("Enter the current market price per share: "))

result = calculate_dividend_yield(dividend, market_price)

print(f"The dividend yield is: {result:.2f}%")
