def calculate_stock_returns(buy_price, sell_price, shares):
    """
    Calculates the total profit or loss and the percentage return or loss.

    Parameters:
    buy_price (float): The price at which the stock was bought.
    sell_price (float): The price at which the stock was sold.
    shares (int): The number of shares bought.

    Returns:
    tuple: Total profit or loss in dollars, Percentage return or loss.
    """
    total_cost = buy_price * shares
    total_sale = sell_price * shares
    profit_loss = total_sale - total_cost
    percent_return_loss = (profit_loss / total_cost) * 100

    return profit_loss, percent_return_loss

def main():
    # Taking user input
    try:
        buy_price = float(input("Enter the buy price of the stock: "))
        sell_price = float(input("Enter the sell price of the stock: "))
        shares = int(input("Enter the number of shares: "))

        # Calculating and displaying the results
        profit_loss, percent_return_loss = calculate_stock_returns(buy_price, sell_price, shares)
        print(f"Total Profit/Loss: ${profit_loss:.2f}")
        print(f"Percentage Return/Loss: {percent_return_loss:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()