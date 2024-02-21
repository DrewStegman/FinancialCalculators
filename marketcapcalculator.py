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
    # Get user input for company details with improved input handling
    try:
        stock_price_input = input("Enter the current stock price (e.g., 123.45): ").replace(',', '')
        total_shares_input = input("Enter the total number of outstanding shares (e.g., 1,000,000): ").replace(',', '')

        # Convert sanitized inputs to appropriate data types
        stock_price = float(stock_price_input)
        total_shares = int(total_shares_input)

        # Calculate market capitalization
        market_cap = calculate_market_cap(stock_price, total_shares)

        # Display result with improved formatting
        print(f"\nMarket Capitalization: ${market_cap:,.2f}")

    except ValueError:
        print("Invalid input. Please ensure you enter numeric values correctly formatted.")

if __name__ == "__main__":
    main()
