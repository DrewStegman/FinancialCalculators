def compound_interest(principal, annual_rate, years):
    """
    Calculate the compound interest for the principal without additional contributions.
    """
    rate = annual_rate / 100
    amount = principal * (1 + rate) ** years
    return amount

def future_value_of_annual_investments(monthly_investment, annual_rate, years):
    """
    Calculate the future value of annual investments (sum of monthly investments over each year).
    """
    rate = annual_rate / 100
    annual_investment = monthly_investment * 12
    future_value = 0
    for year in range(1, years + 1):  # Ensure years is already an integer
        future_value += annual_investment * (1 + rate) ** (years - year)
    return future_value

def total_investment_future_value(principal, monthly_investment, annual_rate, years):
    """
    Calculate the total future value with both initial principal and regular annual investments.
    """
    principal_future_value = compound_interest(principal, annual_rate, years)
    investments_future_value = future_value_of_annual_investments(monthly_investment, annual_rate, years)
    return principal_future_value + investments_future_value

def main():
    print("Welcome to the Compound Interest Calculator")
    try:
        principal_input = input("Enter the initial principal amount (if any): ").replace(',', '')
        monthly_investment_input = input("Enter the monthly investment amount (if any): ").replace(',', '')
        annual_rate_input = input("Enter the annual interest rate (percentage): ").replace(',', '')
        years_input = input("Enter the number of years for the investment: ").replace(',', '')

        # Convert sanitized inputs to appropriate data types
        principal = float(principal_input)
        monthly_investment = float(monthly_investment_input)
        annual_rate = float(annual_rate_input)
        years = int(years_input)

        # Calculating the compound interest
        final_amount = total_investment_future_value(principal, monthly_investment, annual_rate, years)
        
        print(f"The final amount after {years} years is: ${final_amount:,.2f}")  # Formatted to include commas for thousands

    except ValueError:
        print("Invalid input. Please ensure all values are entered correctly as numeric values.")

if __name__ == "__main__":
    main()








