ddef calculate_ddm(dividend_per_share, cost_of_equity, dividend_growth_rate):
    """
    Calculate the fair value of a stock using the Dividend Discount Model.

    :param dividend_per_share: Annual dividend payments per share
    :param cost_of_equity: Required rate of return
    :param dividend_growth_rate: Expected growth rate of the dividends
    :return: Fair value of the stock
    """
    fair_value = dividend_per_share / (cost_of_equity - dividend_growth_rate)
    return fair_value

def get_float_input(prompt):
    """
    Get a float input from the user, ensuring that the input is a valid number.

    :param prompt: Input prompt message
    :return: Float input from the user
    """
    while True:
        try:
            user_input = input(prompt)
            # Remove any commas and convert to float
            return float(user_input.replace(',', ''))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Dividend Discount Model (DDM) Calculator!")
    dividend_per_share = get_float_input("Enter the annual dividend per share (e.g., 1.50): ")
    cost_of_equity = get_float_input("Enter the required rate of return (e.g., 0.08 for 8%): ")
    dividend_growth_rate = get_float_input("Enter the expected dividend growth rate (e.g., 0.03 for 3%): ")

    fair_value = calculate_ddm(dividend_per_share, cost_of_equity, dividend_growth_rate)

    print(f"\nEstimated Fair Value of the Stock: ${fair_value:.2f}")

if __name__ == "__main__":
    main()
