def calculate_average_cost(total_cost, total_shares):
    """
    Calculate the average cost per share of a stock.

    Parameters:
    - total_cost (float): Total cost of the stock investment.
    - total_shares (int): Total number of shares.

    Returns:
    - float: Average cost per share.
    """
    if total_shares == 0:
        return 0  # To avoid division by zero if there are no shares

    average_cost = total_cost / total_shares
    return average_cost

# Example usage:
total_cost = float(input("Enter the total cost of the stock investment: "))
total_shares = int(input("Enter the total number of shares: "))

average_cost_per_share = calculate_average_cost(total_cost, total_shares)

print(f"The average cost per share is: ${average_cost_per_share:.2f}")
