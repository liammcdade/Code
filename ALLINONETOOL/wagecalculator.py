def calculate_income_tax(income):
    """Calculate UK income tax based on the tax bands for 2024/25."""
    # Define tax bands and rates for 2024/25
    personal_allowance = 12570
    bands = [(50270, 0.20), (125140, 0.40), (float('inf'), 0.45)]

    # Calculate income tax
    tax = 0
    remaining_income = income

    # Apply personal allowance
    if remaining_income > 100000:
        personal_allowance = max(0, personal_allowance - (remaining_income - 100000) / 2)
    remaining_income -= personal_allowance

    for band, rate in bands:
        if remaining_income > 0:
            taxable_amount = min(remaining_income, band - personal_allowance)
            tax += taxable_amount * rate
            remaining_income -= taxable_amount
            personal_allowance = band

    return tax

def calculate_nic(income):
    """Calculate UK National Insurance contributions for 2024/25."""
    # Define NIC bands and rates for 2024/25
    primary_threshold = 12570
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
        nic_above_upper_limit = (income - upper_earnings_limit) * rate_above_upper_limit
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