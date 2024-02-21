def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Total number of monthly payments
    total_payments = loan_term_years * 12

    # Monthly mortgage payment calculation using the loan formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-total_payments)

    return monthly_payment

def main():
    # Get user input for loan details
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    loan_term_years = int(input("Enter the loan term in years: "))

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)

    # Display result
    print("\nMonthly Mortgage Payment: $", round(monthly_payment, 2))

if __name__ == "__main__":
    main()
