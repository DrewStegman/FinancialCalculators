def calculate_cagr(initial_value, final_value, years):
    """
    Calculate the Compound Annual Growth Rate (CAGR) for a stock investment.

    Parameters:
    - initial_value (float): Initial value of the investment.
    - final_value (float): Final value of the investment.
    - years (float): Investment period in years.

    Returns:
    - float: CAGR.
    """
    if initial_value == 0 or years == 0:
        return 0  # To avoid division by zero

    cagr = (final_value / initial_value) ** (1 / years) - 1
    return cagr

# Example usage:
initial_value_str = input("Enter the initial value of the investment: $").replace(',', '')
final_value_str = input("Enter the final value of the investment: $").replace(',', '')
years = float(input("Enter the investment period in years (e.g., 2.5): "))

# Convert the inputs to float, handling the commas
initial_value = float(initial_value_str)
final_value = float(final_value_str)

cagr_result = calculate_cagr(initial_value, final_value, years)

print(f"The Compound Annual Growth Rate (CAGR) is: {cagr_result * 100:.2f}%")
