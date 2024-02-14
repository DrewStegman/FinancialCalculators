def calculate_market_cap(stock_price, total_shares):
    """
    Calculate market capitalization.

    Parameters:
    - stock_price (float): Current stock price.
    - total_shares (int): Total number of outstanding shares.

    Returns:
    - float: Market capitalization.
    """
    market_cap = stock_price * total_shares
    return market_cap

def main():
    # Get user input for company details
    stock_price = float(input("Enter the current stock price: "))
    total_shares = int(input("Enter the total number of outstanding shares: "))

    # Calculate market capitalization
    market_cap = calculate_market_cap(stock_price, total_shares)

    # Display result
    print("\nMarket Capitalization: $", round(market_cap, 2))

if __name__ == "__main__":
    main()
