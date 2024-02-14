def calculate_net_worth(assets, liabilities):
    """
    Calculate net worth by subtracting liabilities from assets.

    Parameters:
    - assets (float): Total value of assets.
    - liabilities (float): Total value of liabilities.

    Returns:
    - float: Net worth.
    """
    net_worth = assets - liabilities
    return net_worth

def main():
    # Get user input for asset and liability values
    assets_input = input("Enter the total value of assets ($): ")
    liabilities_input = input("Enter the total value of liabilities ($): ")

    # Remove commas and convert to float
    assets_value = float(assets_input.replace('$', '').replace(',', ''))
    liabilities_value = float(liabilities_input.replace('$', '').replace(',', ''))

    # Calculate net worth
    result = calculate_net_worth(assets_value, liabilities_value)

    # Display result with $ and comma
    formatted_result = "${:,.2f}".format(result)
    print(f"The net worth is: {formatted_result}")

if __name__ == "__main__":
    main()
