def quick_ratio(current_assets, inventories, current_liabilities):
    quick_assets = current_assets - inventories
    return quick_assets / current_liabilities if current_liabilities != 0 else 'Undefined'

def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities if current_liabilities != 0 else 'Undefined'

def debt_to_equity_ratio(total_liabilities, shareholder_equity):
    return total_liabilities / shareholder_equity if shareholder_equity != 0 else 'Undefined'

# Collecting input from the user
print("Please enter the following financial data for the company:")

current_assets = float(input("Total Current Assets: "))
inventories = float(input("Total Inventories: "))
current_liabilities = float(input("Total Current Liabilities: "))
total_liabilities = float(input("Total Liabilities: "))
shareholder_equity = float(input("Shareholder Equity: "))

# Calculating ratios
quick_ratio_result = quick_ratio(current_assets, inventories, current_liabilities)
current_ratio_result = current_ratio(current_assets, current_liabilities)
debt_to_equity_ratio_result = debt_to_equity_ratio(total_liabilities, shareholder_equity)

# Displaying the results
print(f"\nCalculated Financial Ratios:")
print(f"Quick Ratio: {quick_ratio_result:.2f}")
print(f"Current Ratio: {current_ratio_result:.2f}")
print(f"Debt to Equity Ratio: {debt_to_equity_ratio_result:.2f}")