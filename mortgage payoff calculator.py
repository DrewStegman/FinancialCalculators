def mortgage_payoff_calculator(loan_amount, annual_interest_rate, loan_term_years):
    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Total number of monthly payments
    total_payments = loan_term_years * 12

    # Monthly mortgage payment calculation using the loan formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-total_payments)

    # Amortization schedule
    remaining_balance = loan_amount
    amortization_schedule = []

    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_schedule.append({
            'Month': month,
            'Monthly Payment': "{:,.2f}".format(monthly_payment),
            'Principal Payment': "{:,.2f}".format(principal_payment),
            'Interest Payment': "{:,.2f}".format(interest_payment),
            'Remaining Balance': "{:,.2f}".format(remaining_balance if remaining_balance > 0 else 0)
        })

    return amortization_schedule

def main():
    # Get user input for loan details
    loan_amount_input = input("Enter the loan amount (e.g., 250,000): ")
    annual_interest_rate_input = input("Enter the annual interest rate as a percentage (e.g., 4.5): ")
    loan_term_years_input = input("Enter the loan term in years (e.g., 30): ")

    # Remove commas from inputs and convert to appropriate data types
    loan_amount = float(loan_amount_input.replace(',', ''))
    annual_interest_rate = float(annual_interest_rate_input)
    loan_term_years = int(loan_term_years_input)

    # Calculate and display amortization schedule
    schedule = mortgage_payoff_calculator(loan_amount, annual_interest_rate, loan_term_years)

    print("\nAmortization Schedule:")
    print("{:<10} {:<20} {:<20} {:<20} {:<20}".format('Month', 'Monthly Payment', 'Principal Payment', 'Interest Payment', 'Remaining Balance'))
    for entry in schedule:
        print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(
            entry['Month'],
            entry['Monthly Payment'],
            entry['Principal Payment'],
            entry['Interest Payment'],
            entry['Remaining Balance']
        ))

if __name__ == "__main__":
    main()
