def calculate_income_tax(income):
    """Calculate UK income tax based on the tax bands."""
    # Define tax bands and rates
    bands = [(12570, 0.20), (50270, 0.40), (150000, 0.45)]

    # Calculate income tax
    tax = 0
    remaining_income = income

    for band, rate in bands:
        if remaining_income > band:
            taxable_amount = min(remaining_income, band)
            tax += taxable_amount * rate
            remaining_income -= band

    return tax

def calculate_nic(income):
    """Calculate UK National Insurance contributions."""
    # Define NIC bands and rates
    primary_threshold = 9568
    upper_earnings_limit = 50270
    rate_below_upper_limit = 0.12
    rate_above_upper_limit = 0.02

    # Calculate NIC
    if income <= primary_threshold:
        return 0
    elif income <= upper_earnings_limit:
        return (income - primary_threshold) * rate_below_upper_limit
    else:
        nic_below_upper_limit = (upper_earnings_limit - primary_threshold) * rate_below_upper_limit
        nic_above_upper_limit = max(0, income - upper_earnings_limit) * rate_above_upper_limit
        return nic_below_upper_limit + nic_above_upper_limit

def calculate_total_deductions(income):
    """Calculate total deductions (income tax + NIC)."""
    income_tax = calculate_income_tax(income)
    nic = calculate_nic(income)
    return income_tax + nic

def calculate_net_income(income):
    """Calculate net income after deductions."""
    deductions = calculate_total_deductions(income)
    return income - deductions

def main():
    print("Welcome to the UK Wage Calculator!")

    # Get annual income from the user
    try:
        annual_income = float(input("Enter annual income: £"))
    except ValueError:
        print("Invalid input. Please enter a valid annual income.")
        return

    # Calculate and display net income
    net_income = calculate_net_income(annual_income)

    print(f"Net income after tax and NIC: £{net_income:.2f}")

if __name__ == "__main__":
    main()
