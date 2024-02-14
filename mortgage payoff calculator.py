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
            'Monthly Payment': round(monthly_payment, 2),
            'Principal Payment': round(principal_payment, 2),
            'Interest Payment': round(interest_payment, 2),
            'Remaining Balance': round(remaining_balance, 2)
        })

    return amortization_schedule

def main():
    # Get user input for loan details
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    loan_term_years = int(input("Enter the loan term in years: "))

    # Calculate and display amortization schedule
    schedule = mortgage_payoff_calculator(loan_amount, annual_interest_rate, loan_term_years)

    print("\nAmortization Schedule:")
    print("{:<10} {:<15} {:<15} {:<15} {:<20}".format('Month', 'Monthly Payment', 'Principal Payment', 'Interest Payment', 'Remaining Balance'))
    for entry in schedule:
        print("{:<10} {:<15} {:<15} {:<15} {:<20}".format(
            entry['Month'],
            entry['Monthly Payment'],
            entry['Principal Payment'],
            entry['Interest Payment'],
            entry['Remaining Balance']
        ))

if __name__ == "__main__":
    main()
