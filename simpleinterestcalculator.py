def calculate_simple_interest(principal, annual_rate, time_years):
    return (principal * annual_rate * time_years) / 100

def get_float_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Remove commas and convert to float
            return float(user_input.replace(',', ''))
        except ValueError:
            print("Please enter a valid number.")

def format_currency(value):
    return "${:,.2f}".format(value)

def main():
    print("Welcome to the Simple Interest Calculator!")

    principal = get_float_input("Enter the principal amount (e.g., 1,000): ")
    annual_rate = get_float_input("Enter the annual interest rate (in %, e.g., 5): ")
    time_years = get_float_input("Enter the time in years: ")

    interest = calculate_simple_interest(principal, annual_rate, time_years)
    print(f"The simple interest is: {format_currency(interest)}")

if __name__ == "__main__":
    main()
