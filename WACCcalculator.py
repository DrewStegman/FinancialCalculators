def calculate_wacc(market_value_equity, market_value_debt, cost_of_equity, cost_of_debt, tax_rate):
    total_value = market_value_equity + market_value_debt
    weight_of_equity = market_value_equity / total_value
    weight_of_debt = market_value_debt / total_value
    after_tax_cost_of_debt = cost_of_debt * (1 - tax_rate)
    wacc = (weight_of_equity * cost_of_equity) + (weight_of_debt * after_tax_cost_of_debt)
    return wacc

def calculate_cost_of_equity(risk_free_rate, beta, expected_market_return):
    return risk_free_rate + beta * (expected_market_return - risk_free_rate)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the WACC Calculator!")
    risk_free_rate = get_float_input("Enter the risk-free rate (e.g., 0.02 for 2%): ")
    beta = get_float_input("Enter the beta of the stock: ")
    expected_market_return = get_float_input("Enter the expected market return (e.g., 0.08 for 8%): ")
    market_value_equity = get_float_input("Enter the market value of the company's equity: ")
    market_value_debt = get_float_input("Enter the market value of the company's debt: ")
    cost_of_debt = get_float_input("Enter the cost of debt (e.g., 0.05 for 5%): ")
    tax_rate = get_float_input("Enter the company's tax rate (e.g., 0.3 for 30%): ")

    cost_of_equity = calculate_cost_of_equity(risk_free_rate, beta, expected_market_return)
    wacc = calculate_wacc(market_value_equity, market_value_debt, cost_of_equity, cost_of_debt, tax_rate)

    print(f"\nCost of Equity: {cost_of_equity:.2%}")
    print(f"WACC: {wacc:.2%}")

if __name__ == "__main__":
    main()
